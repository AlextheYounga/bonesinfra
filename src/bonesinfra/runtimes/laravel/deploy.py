from pathlib import Path

from pyinfra import host

from bonesinfra.infra.toml_store import load_runtime_config
from bonesinfra.infra.utils import unflatten
from bonesinfra.runtimes.laravel import apparmor, nginx, php_fpm, php_packages, php_repo


def deploy():
    here = Path(__file__).parent
    data = unflatten(host.data.dict())
    runtime = load_runtime_config(__file__)
    php_version = runtime.get("php_version", "8.3")
    paths = data["paths"]

    php_repo.add_php_apt_source()
    php_packages.install_php(php_version)

    php_fpm.setup_storage_directories(paths, data)
    php_fpm.setup_pool(here, data, paths, php_version)
    apparmor.setup_php_fpm(data, here)
    nginx.setup(here, data, paths)
