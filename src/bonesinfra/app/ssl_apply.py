import sys

from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.ssl.plan import deploy_ssl
from bonesinfra.domain.context import DeployContext


def apply(config_path: str) -> None:
    ctx = DeployContext.from_files(config_path)
    if not ctx.config.domain or not ctx.config.email:
        print("Error: ssl.domain and ssl.email are required in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_plan(deploy_ssl, ctx)
