import sys

from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.ssl.plan import deploy_ssl
from bonesinfra.domain.context import DeployContext


def apply(config_path: str, ssh_user: str = "root") -> None:
    ctx = DeployContext.from_files(config_path, ssh_user=ssh_user)
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    if not ctx.flat_data.get("ssl_domain") or not ctx.flat_data.get("ssl_email"):
        print("Error: ssl.domain and ssl.email are required in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_plan(deploy_ssl, ctx)
