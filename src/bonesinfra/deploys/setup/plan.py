from pathlib import Path

from pyinfra import host

from bonesinfra.deploys.setup import bonesremote, directories, firewall, packages, placeholder, users
from bonesinfra.deploys.setup.packages import BASE_SYSTEM_PACKAGES, SUPPLEMENTARY_PACKAGES
from bonesinfra.infra.utils import unflatten


def deploy():
    data = unflatten(host.data.dict())
    paths = data.get("paths", {})
    here = Path(__file__).parent.parent.parent
    all_pkgs = BASE_SYSTEM_PACKAGES + SUPPLEMENTARY_PACKAGES

    packages.install_system(all_pkgs)
    users.install_rust()
    users.ensure_users_and_groups(data)
    directories.setup_repo_and_project(data, paths)
    placeholder.seed(data, paths, here)
    firewall.configure(data)
    bonesremote.install_authorized_key(data)
    bonesremote.install()
