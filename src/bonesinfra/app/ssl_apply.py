import sys

from bonesinfra.deploys.ssl.plan import deploy_ssl
from bonesinfra.domain.context import DeployContext
from bonesinfra.infra.pyinfra_runner import run as run_deploy


def apply(config_path: str, ssh_user: str = "root") -> None:
    ctx = DeployContext.from_files(config_path, ssh_user=ssh_user)
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    ssl_domain = ctx.flat_data.get("ssl_domain")
    ssl_email = ctx.flat_data.get("ssl_email")
    if not ssl_domain:
        print("Error: ssl.domain is required in bones.toml", file=sys.stderr)
        sys.exit(3)
    if not ssl_email:
        print("Error: ssl.email is required in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_deploy(
        hostname=ctx.host,
        ssh_user=ctx.ssh_user,
        ssh_port=ctx.ssh_port,
        data=ctx.flat_data,
        deploy=deploy_ssl,
    )
