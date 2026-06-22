from shlex import quote

from pyinfra import host
from pyinfra.facts.server import Users
from pyinfra.operations import server


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


def ensure_users_and_groups(ctx):
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
        name="Ensure release-read group exists",
        group=ctx.runtime.release_group,
        _sudo=True,
    )

    _ensure_group_membership(ctx.config.deploy_user, ctx.runtime.runtime_group)

    existing_user = host.get_fact(Users).get(ctx.runtime.runtime_user)

    if existing_user is None:
        server.user(
            name="Ensure runtime user exists with groups",
            user=ctx.runtime.runtime_user,
            system=True,
            home="/nonexistent",
            shell="/usr/sbin/nologin",
            create_home=False,
            groups=[ctx.runtime.runtime_group, ctx.runtime.release_group],
            _sudo=True,
        )
        return

    required_groups = []
    for group in (ctx.runtime.runtime_group, ctx.runtime.release_group):
        if group not in required_groups:
            required_groups.append(group)

    for group in required_groups:
        if group != existing_user["group"] and group not in existing_user["groups"]:
            _ensure_group_membership(ctx.runtime.runtime_user, group)


def install_authorized_key(ctx):
    deploy_user = ctx.config.deploy_user
    ssh_user = ctx.config.ssh_user
    server.shell(
        name=f"Copy {ssh_user} SSH key to deploy user {deploy_user}",
        commands=[
            f"install -d -o {deploy_user} -g {deploy_user} -m 0700 /home/{deploy_user}/.ssh",
            (
                f'src=$(eval echo ~{ssh_user}/.ssh/authorized_keys); '
                f'[ -f "$src" ] || {{ echo "ERROR: $src not found" >&2; exit 1; }}; '
                f'cp "$src" /home/{deploy_user}/.ssh/authorized_keys'
            ),
            f"chown {deploy_user}:{deploy_user} /home/{deploy_user}/.ssh/authorized_keys",
            f"chmod 0600 /home/{deploy_user}/.ssh/authorized_keys",
        ],
        _sudo=True,
    )
