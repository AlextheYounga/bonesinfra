from pathlib import Path

from bonesinfra.deploys.setup import bonesremote, directories, firewall, packages, placeholder, users
from bonesinfra.deploys.setup.packages import BASE_SYSTEM_PACKAGES, SUPPLEMENTARY_PACKAGES
from bonesinfra.domain.paths import DeploymentPaths


def deploy_setup(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent
    all_pkgs = BASE_SYSTEM_PACKAGES + SUPPLEMENTARY_PACKAGES

    packages.install_system(all_pkgs)
    users.install_rust()
    users.ensure_users_and_groups(ctx)
    directories.setup_repo_and_project(ctx, paths)
    placeholder.seed(ctx, paths, here)
    firewall.configure(ctx)
    bonesremote.install_authorized_key(ctx)
    bonesremote.install()
