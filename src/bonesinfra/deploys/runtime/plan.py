from pathlib import Path

from pyinfra import host

from bonesinfra.deploys.runtime import apparmor, doctor, nginx, packages, template_runtime
from bonesinfra.infra.utils import unflatten


def deploy():
    data = unflatten(host.data.dict())
    paths = data.get("paths", {})
    here = Path(__file__).parent.parent.parent

    packages.install_apt(data)
    apparmor.setup(data, paths, here)
    nginx.setup(data, paths, here)
    template_runtime.load(data)
    doctor.run(data)
