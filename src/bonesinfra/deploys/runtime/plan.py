from pathlib import Path

from bonesinfra.deploys.runtime import apparmor, doctor, nginx, packages, template_runtime
from bonesinfra.domain.paths import DeploymentPaths


def deploy_runtime(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent

    packages.install_apt(ctx)
    apparmor.setup(ctx, paths, here)
    nginx.setup(ctx, paths, here)
    template_runtime.load(ctx)
    nginx.start_services(paths)
    doctor.run(ctx)
