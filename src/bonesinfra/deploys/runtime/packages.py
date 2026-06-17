from pyinfra.operations import apt


def install_apt(data):
    pkgs = data.get("runtime_apt_packages", [])
    if not pkgs:
        return
    apt.packages(
        name="Install runtime apt packages",
        packages=pkgs,
        present=True,
        update=True,
        cache_time=3600,
        _sudo=True,
    )
