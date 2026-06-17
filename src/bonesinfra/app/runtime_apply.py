import sys

from bonesinfra.deploys.runtime.plan import deploy
from bonesinfra.domain.context import DeployContext
from bonesinfra.infra.pyinfra_runner import run as run_deploy


def apply(config_path: str, runtime_config_path: str, ssh_user: str) -> None:
    ctx = DeployContext.from_files(config_path, runtime_config_path, ssh_user)
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_deploy(
        hostname=ctx.host,
        ssh_user=ctx.ssh_user,
        ssh_port=ctx.ssh_port,
        data=ctx.flat_data,
        deploy=deploy,
    )
