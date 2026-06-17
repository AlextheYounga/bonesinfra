from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.setup.plan import deploy_setup
from bonesinfra.domain.context import DeployContext


def apply(config_path: str, ssh_user: str = "root") -> None:
    ctx = DeployContext.from_files(config_path, ssh_user=ssh_user)
    run_plan(deploy_setup, ctx)
