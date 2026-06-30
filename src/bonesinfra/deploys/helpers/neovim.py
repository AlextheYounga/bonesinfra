from pyinfra.operations import files, server

from bonesinfra.domain.paths import ASSETS_DIR

NVIM_CONFIG_DIR = "/etc/xdg/nvim"
INSTALL_SCRIPT = "/usr/local/lib/bonesinfra/install-neovim.sh"


def install():
    files.put(
        name="Install Neovim helper script",
        src=str(ASSETS_DIR / "scripts/install-neovim.sh"),
        dest=INSTALL_SCRIPT,
        user="root",
        group="root",
        mode="0755",
        _sudo=True,
    )

    server.shell(
        name="Install Neovim > 0.11 from official release",
        commands=[INSTALL_SCRIPT],
        _sudo=True,
    )

    files.sync(
        name="Install shared Neovim config",
        src=str(ASSETS_DIR / "nvim"),
        dest=NVIM_CONFIG_DIR,
        user="root",
        group="root",
        mode="0644",
        dir_mode="0755",
        delete=False,
        _sudo=True,
    )
