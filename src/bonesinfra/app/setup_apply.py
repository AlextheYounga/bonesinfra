from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.setup.plan import deploy_setup
from bonesinfra.domain.context import DeployContext


def apply(config_path: str) -> None:
    ctx = DeployContext.from_files(config_path)
    run_plan(deploy_setup, ctx)
