from pyinfra.operations import server


def install_rust():
    server.shell(
        name="Install rustup and cargo",
        commands=["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal"],
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
