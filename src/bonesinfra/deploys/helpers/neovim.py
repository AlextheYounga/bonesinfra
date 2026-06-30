from pyinfra.operations import files, server

from bonesinfra.domain.paths import ASSETS_DIR

NVIM_CONFIG_DIR = "/etc/xdg/nvim"
INSTALL_SCRIPT = "/usr/local/lib/bonesinfra/install-neovim.sh"
NVIM_CONFIG_REPO = "https://github.com/AlextheYounga/myneovim.git"


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

    server.shell(
        name="Install shared Neovim config repo",
        commands=[
            (
                f"if [ -d {NVIM_CONFIG_DIR}/.git ]; then "
                f"git -C {NVIM_CONFIG_DIR} fetch --depth=1 origin && "
                f"git -C {NVIM_CONFIG_DIR} reset --hard FETCH_HEAD; "
                "else "
                f"rm -rf {NVIM_CONFIG_DIR} && git clone --depth=1 {NVIM_CONFIG_REPO} {NVIM_CONFIG_DIR}; "
                "fi"
            ),
            f"chown -R root:root {NVIM_CONFIG_DIR}",
        ],
        _sudo=True,
    )

    files.directory(
        name="Ensure shared Neovim config permissions",
        path=NVIM_CONFIG_DIR,
        user="root",
        group="root",
        mode="0755",
        _sudo=True,
    )
