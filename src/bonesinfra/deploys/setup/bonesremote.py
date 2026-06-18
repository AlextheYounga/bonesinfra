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


def install_authorized_key(ctx):
    if not ctx.runtime.runtime_data.get("deploy_authorized_key"):
        return
    server.user(
        name="Ensure deploy user authorized key is installed",
        user=ctx.config.deploy_user,
        public_keys=[ctx.runtime.runtime_data["deploy_authorized_key"]],
        _sudo=True,
    )
