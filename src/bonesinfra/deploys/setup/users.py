from shlex import quote

from pyinfra import host
from pyinfra.facts.server import Users
from pyinfra.operations import server

from bonesinfra.infra.deploy_helpers import mkdir

BUILD_USER_HOME_ROOT = "/var/lib/bonesdeploy/users"


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


def _validate_subid_ranges(build_user: str):
    q_subid_prefix = quote(f"^{build_user}:")
    server.shell(
        name=f"Validate subuid/subgid ranges for {build_user}",
        commands=[
            f"grep -q {q_subid_prefix} /etc/subuid",
            f"grep -q {q_subid_prefix} /etc/subgid",
        ],
        _sudo=True,
    )


def _validate_rootless_podman(build_user: str, build_group: str, build_home: str):
    q_build_user = quote(build_user)
    q_build_group = quote(build_group)
    q_build_home = quote(build_home)
    server.shell(
        name=f"Validate rootless podman for {build_user}",
        commands=[
            (
                f"uid=$(id -u {q_build_user})"
                f" && install -d -o {q_build_user} -g {q_build_group} -m 0700 /run/user/$uid"
                f" && runuser -u {q_build_user} -- env"
                f" HOME={q_build_home} XDG_RUNTIME_DIR=/run/user/$uid"
                " podman info --format '{{.Host.Security.Rootless}}'"
                " | grep -Fx true"
            )
        ],
        _sudo=True,
    )


def ensure_users_and_groups(ctx):
    build_user = build_user_for(ctx.config.project_name)
    build_group = build_group_for(ctx.config.project_name)
    build_home = build_home_for(ctx.config.project_name)

    server.user(
        name="Ensure deploy user exists",
        user=ctx.config.deploy_user,
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

    server.user(
        name="Ensure build user exists",
        user=build_user,
        group=build_group,
        home="/nonexistent",
        shell="/usr/sbin/nologin",
        create_home=False,
        _sudo=True,
    )

    mkdir(
        name="Ensure bonesdeploy user home root exists",
        path=BUILD_USER_HOME_ROOT,
    )
    mkdir(
        name=f"Ensure podman pseudo-home for {build_user}",
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
    _validate_subid_ranges(build_user)
    _validate_rootless_podman(build_user, build_group, build_home)


def install_authorized_key(ctx):
    deploy_user = ctx.config.deploy_user
    ssh_user = ctx.config.ssh_user
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
