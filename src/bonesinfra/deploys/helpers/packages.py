from pyinfra.operations import apt, server

HELPER_APT_PACKAGES: list[str] = [
    "age",
    "apt-listchanges",
    "apt-transport-https",
    "automysqlbackup",
    "autossh",
    "bash-completion",
    "bat",
    "btop",
    "borgbackup",
    "fastfetch",
    "fd-find",
    "fzf",
    "gnupg",
    "iftop",
    "inotify-tools",
    "iotop",
    "jdupes",
    "jq",
    "lsb-release",
    "lsof",
    "moreutils",
    "mutt",
    "ncdu",
    "powerstat",
    "powertop",
    "rename",
    "ripgrep",
    "smartmontools",
    "sysbench",
    "sysstat",
    "telnet",
    "tmux",
    "tree",
]


def install_helper_apt_packages(packages):
    apt.packages(
        name="Install supplementary helper apt packages",
        packages=packages,
        present=True,
        update=True,
        cache_time=3600,
        _sudo=True,
    )


def install_debian_command_aliases():
    server.shell(
        name="Install Debian helper command aliases",
        commands=[
            "install -d -m 0755 /usr/local/bin",
            (
                "if command -v batcat >/dev/null 2>&1 && [ ! -x /usr/local/bin/bat ]; "
                'then ln -sf "$(command -v batcat)" /usr/local/bin/bat; fi'
            ),
            (
                "if command -v fdfind >/dev/null 2>&1 && [ ! -x /usr/local/bin/fd ]; "
                'then ln -sf "$(command -v fdfind)" /usr/local/bin/fd; fi'
            ),
        ],
        _sudo=True,
    )
