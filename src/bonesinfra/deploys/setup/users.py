from shlex import quote

from pyinfra import host
from pyinfra.facts.hardware import Cpus
from pyinfra.facts.server import Users
from pyinfra.operations import server

from bonesinfra.deploys.setup.image_store import BASE_IMAGE
from bonesinfra.domain.context import DEFAULT_BUILD_CPU_QUOTA_PERCENT, DEPLOY_USER
from bonesinfra.domain.paths import ASSETS_DIR, IMAGE_STORE_GRAPH_ROOT
from bonesinfra.infra.deploy_helpers import mkdir, render

BUILD_USER_HOME_ROOT = "/var/lib/bonesdeploy/users"
BUILD_SYSTEMD_STAGING_ROOT = "/run/bonesdeploy"


def install_rust():
    server.shell(
        name="Install rustup and cargo",
        commands=["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal"],
        _sudo=True,
    )


def _ensure_group_membership(user, group):
    q_user = quote(user)
    q_group = quote(group)
    server.shell(
        name=f"Ensure {user} is a member of {group}",
        commands=[f"id -nG {q_user} | tr ' ' '\\n' | grep -Fxq {q_group} || gpasswd -a {q_user} {q_group}"],
        _sudo=True,
    )


def build_user_for(project_name: str) -> str:
    return f"{project_name}-build"


def build_group_for(project_name: str) -> str:
    return build_user_for(project_name)


def build_home_for(project_name: str) -> str:
    return f"{BUILD_USER_HOME_ROOT}/{build_user_for(project_name)}"


def cpu_quota_for(online_cpu_count: int, per_cpu_percent: int = DEFAULT_BUILD_CPU_QUOTA_PERCENT) -> str:
    if online_cpu_count < 1:
        raise ValueError("online_cpu_count must be positive")
    return f"{online_cpu_count * per_cpu_percent}%"


def configure_build_user_storage(project_name: str):
    build_user = build_user_for(project_name)
    build_group = build_group_for(project_name)
    build_home = build_home_for(project_name)
    config_dir = f"{build_home}/.config/containers"
    storage_conf = f"{config_dir}/storage.conf"

    mkdir(
        name=f"Ensure containers config directory for {build_user}",
        path=config_dir,
        user=build_user,
        group=build_group,
        mode="0700",
    )
    render(
        name=f"Install storage.conf for {build_user}",
        src=ASSETS_DIR / "podman/build-user-storage.conf.j2",
        dest=storage_conf,
        user=build_user,
        group=build_group,
        mode="0600",
        additional_image_store=IMAGE_STORE_GRAPH_ROOT,
    )


def ensure_users_and_groups(ctx):
    build_user = build_user_for(ctx.app.project_name)
    build_group = build_group_for(ctx.app.project_name)
    build_home = build_home_for(ctx.app.project_name)
    resources = ctx.build.resources
    cpu_quota = cpu_quota_for(host.get_fact(Cpus), resources.cpu_quota_percent)
    staged_dropin = f"{BUILD_SYSTEMD_STAGING_ROOT}/{build_user}.slice.conf"

    server.user(
        name="Ensure deploy user exists",
        user=DEPLOY_USER,
        shell="/bin/bash",
        ensure_home=True,
        _sudo=True,
    )

    server.group(
        name="Ensure runtime group exists",
        group=ctx.runtime.runtime_group,
        _sudo=True,
    )

    server.group(
        name="Ensure build group exists",
        group=build_group,
        _sudo=True,
    )

    existing_user = host.get_fact(Users).get(ctx.runtime.runtime_user)

    if existing_user is None:
        server.user(
            name="Ensure runtime user exists with groups",
            user=ctx.runtime.runtime_user,
            system=True,
            home="/nonexistent",
            shell="/usr/sbin/nologin",
            create_home=False,
            groups=[ctx.runtime.runtime_group],
            _sudo=True,
        )
    elif (
        ctx.runtime.runtime_group != existing_user["group"] and ctx.runtime.runtime_group not in existing_user["groups"]
    ):
        _ensure_group_membership(ctx.runtime.runtime_user, ctx.runtime.runtime_group)

    mkdir(
        name="Ensure bonesdeploy user home root exists",
        path=BUILD_USER_HOME_ROOT,
    )

    # useradd allocates unused subuid/subgid ranges for new non-system users.
    # ponytail: damaged existing mappings fail verification; repair them with
    # administrator-selected usermod ranges rather than guessing new ownership.
    server.user(
        name="Ensure build user exists",
        user=build_user,
        group=build_group,
        home=build_home,
        shell="/usr/sbin/nologin",
        create_home=True,
        _sudo=True,
    )

    mkdir(
        name=f"Ensure persistent home for {build_user}",
        path=build_home,
        user=build_user,
        group=build_group,
        mode="0700",
    )
    server.shell(
        name=f"Enable linger for {build_user}",
        commands=[f"loginctl enable-linger {quote(build_user)}"],
        _sudo=True,
    )
    server.shell(
        name=f"Start systemd user manager for {build_user}",
        commands=[f"systemctl start user@$(id -u {quote(build_user)}).service"],
        _sudo=True,
    )
    mkdir(
        name="Ensure systemd drop-in staging directory exists",
        path=BUILD_SYSTEMD_STAGING_ROOT,
    )
    render(
        name=f"Stage resource limits for {build_user}",
        src=ASSETS_DIR / "systemd/bonesdeploy-build.slice.j2",
        dest=staged_dropin,
        cpu_quota=cpu_quota,
        memory_high=f"{resources.memory_high_percent}%",
        memory_max=f"{resources.memory_max_percent}%",
    )
    server.shell(
        name=f"Install and apply resource limits for {build_user}",
        commands=[
            f"slice=user-$(id -u {quote(build_user)}).slice; "
            'dropin="/etc/systemd/system/$slice.d/bonesdeploy-build.conf"; '
            'install -d -m 0755 "${dropin%/*}"; '
            f'cmp -s {quote(staged_dropin)} "$dropin" || {{ '
            f'install -m 0644 {quote(staged_dropin)} "$dropin"; systemctl daemon-reload; '
            f'systemctl set-property --runtime "$slice" CPUQuota={cpu_quota} '
            f"MemoryHigh={resources.memory_high_percent}% MemoryMax={resources.memory_max_percent}%; }}"
        ],
        _sudo=True,
    )
    configure_build_user_storage(ctx.app.project_name)
    server.shell(
        name=f"Verify rootless Podman for {build_user}",
        commands=[
            'getsubids $(id -un) | grep -q . || (echo "ERROR: build user is missing subordinate UIDs" >&2; false)',
            'getsubids -g $(id -un) | grep -q . || (echo "ERROR: build user is missing subordinate GIDs" >&2; false)',
            "loginctl show-user $(id -un) -p Linger --value | grep -qx yes || "
            '(echo "ERROR: build user lingering is disabled" >&2; false)',
            "systemctl is-active --quiet user@$(id -u).service || "
            '(echo "ERROR: build user manager is inactive" >&2; false)',
            'test -S "/run/user/$(id -u)/bus" || (echo "ERROR: build user D-Bus socket is missing" >&2; false)',
            f"HOME={quote(build_home)} XDG_RUNTIME_DIR=/run/user/$(id -u) "
            "podman info --format '{{.Host.Security.Rootless}}' | grep -qx true || "
            '(echo "ERROR: rootless Podman is unavailable" >&2; false)',
        ],
        _sudo=True,
        _sudo_user=build_user,
        _chdir=build_home,
    )
    server.shell(
        name=f"Verify shared image store for {build_user}",
        commands=[
            f"HOME={quote(build_home)} XDG_RUNTIME_DIR=/run/user/$(id -u) "
            f"podman info --format '{{{{.Store.AdditionalImageStores}}}}' | "
            f"grep -qF {quote(IMAGE_STORE_GRAPH_ROOT)} || "
            '(echo "ERROR: shared image store not configured" >&2; false)',
            f"HOME={quote(build_home)} XDG_RUNTIME_DIR=/run/user/$(id -u) "
            f"podman image exists {quote(BASE_IMAGE)} || "
            '(echo "ERROR: base image not found in shared store" >&2; false)',
        ],
        _sudo=True,
        _sudo_user=build_user,
        _chdir=build_home,
    )


def install_authorized_key(ctx):
    deploy_user = DEPLOY_USER
    ssh_user = ctx.app.server.ssh_user
    server.shell(
        name=f"Copy {ssh_user} SSH key to deploy user {deploy_user}",
        commands=[
            f"install -d -o {deploy_user} -g {deploy_user} -m 0700 /home/{deploy_user}/.ssh",
            (
                f"src=$(eval echo ~{ssh_user}/.ssh/authorized_keys); "
                f'[ -f "$src" ] || {{ echo "ERROR: $src not found" >&2; exit 1; }}; '
                f'cp "$src" /home/{deploy_user}/.ssh/authorized_keys'
            ),
            f"chown {deploy_user}:{deploy_user} /home/{deploy_user}/.ssh/authorized_keys",
            f"chmod 0600 /home/{deploy_user}/.ssh/authorized_keys",
        ],
        _sudo=True,
    )
