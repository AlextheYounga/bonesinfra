from pyinfra.operations import server

from bonesinfra.domain.paths import BONESDEPLOY_REPO


def install():
    cargo_bin = "/root/.cargo/bin/cargo"
    server.shell(
        name="Install bonesremote binary",
        commands=[f"{cargo_bin} install --root /usr/local --git {BONESDEPLOY_REPO} bonesremote"],
        _sudo=True,
    )

    server.shell(
        name="Run bonesremote init",
        commands=["/usr/local/bin/bonesremote init"],
        _sudo=True,
    )
