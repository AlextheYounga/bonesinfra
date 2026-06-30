from bonesinfra.deploys.helpers import aptui, crates, neovim, packages, starship
from bonesinfra.deploys.helpers.packages import HELPER_APT_PACKAGES


def deploy_helpers(ctx):
    del ctx
    packages.install_helper_apt_packages(HELPER_APT_PACKAGES)
    packages.install_debian_command_aliases()
    starship.install()
    neovim.install()
    aptui.install_aptui()
    crates.install_helper_crates()
