from pathlib import Path

from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.toml_store import load_runtime_config
from bonesinfra.runtimes.laravel import apparmor, nginx, php_fpm, php_packages, php_repo


def deploy(ctx):
    here = Path(__file__).parent
    runtime = load_runtime_config(__file__)
    php_version = runtime.get("php_version", "8.3")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__

    php_repo.add_php_apt_source()
    php_packages.install_php(php_version)

    php_fpm.setup_storage_directories(paths, ctx)
    apparmor.setup_php_fpm(ctx, here)
    php_fpm.setup_pool(here, ctx, paths, php_version)
    nginx.setup(here, ctx, paths)
