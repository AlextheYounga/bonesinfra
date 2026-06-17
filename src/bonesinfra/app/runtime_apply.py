from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.runtime.plan import deploy_runtime
from bonesinfra.domain.context import DeployContext


def apply(config_path: str, runtime_config_path: str, ssh_user: str) -> None:
    ctx = DeployContext.from_files(config_path, runtime_config_path, ssh_user)
    run_plan(deploy_runtime, ctx)
