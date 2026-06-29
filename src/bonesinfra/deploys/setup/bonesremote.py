from pathlib import Path

from pyinfra.operations import server

from bonesinfra.domain.context import template_data
from bonesinfra.domain.paths import BONESDEPLOY_REPO
from bonesinfra.infra.deploy_helpers import render


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


def install_sudoers(ctx, paths, here):
    render(
        "Install narrow per-site sudoers drop-in",
        here / "assets/sudoers/bonesdeploy.j2",
        paths["sudoers_path"],
        user="root",
        group="root",
        mode="0440",
        **template_data(ctx, paths=paths),
    )
    server.shell(
        name="Validate sudoers drop-in",
        commands=[f"visudo -c -f {Path(paths['sudoers_path'])}"],
        _sudo=True,
    )
