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


def ensure_users_and_groups(data):
    server.user(
        name="Ensure deploy user exists",
        user=data["deploy_user"],
        shell="/bin/bash",
        ensure_home=True,
        _sudo=True,
    )

    server.group(
        name="Ensure runtime group exists",
        group=data["runtime_group"],
        _sudo=True,
    )

    server.group(
        name="Ensure release-read group exists",
        group=data["release_group"],
        _sudo=True,
    )

    existing_user = host.get_fact(Users).get(data["runtime_user"])

    if existing_user is None:
        server.user(
            name="Ensure runtime user exists with groups",
            user=data["runtime_user"],
            system=True,
            home="/nonexistent",
            shell="/usr/sbin/nologin",
            create_home=False,
            groups=[data["runtime_group"], data["release_group"]],
            _sudo=True,
        )
        return

    required_groups = []
    for group in (data["runtime_group"], data["release_group"]):
        if group not in required_groups:
            required_groups.append(group)

    for group in required_groups:
        if group != existing_user["group"] and group not in existing_user["groups"]:
            _ensure_group_membership(data["runtime_user"], group)
