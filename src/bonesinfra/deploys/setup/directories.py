from pathlib import Path
from shlex import quote

from pyinfra.operations import server

from bonesinfra.infra.deploy_helpers import mkdir


def _user_env_command(user, command):
    q_user = quote(user)
    home = f'$(getent passwd {q_user} | cut -d: -f6)'
    return f'HOME={home} XDG_CONFIG_HOME={home}/.config {command}'


def setup_repo_and_project(data, paths):
    mkdir(
        name="Ensure bare repo parent directory exists",
        path=paths["repo_parent"],
        user=data["deploy_user"],
        group=data["deploy_user"],
    )

    server.shell(
        name="Initialize bare git repo",
        commands=[_user_env_command(data["deploy_user"], f"git init --bare {quote(paths['repo'])}")],
        _sudo=True,
        _sudo_user=data["deploy_user"],
    )

    mkdir(
        name="Ensure bare repo bones directory exists",
        path=paths["repo_bones"],
        user=data["deploy_user"],
        group=data["deploy_user"],
    )

    mkdir(
        name="Ensure project root parent directory is traversable",
        path=paths["project_root_parent"],
        mode="0711",
    )

    mkdir(
        name="Ensure project root with setgid for release group",
        path=data["project_root"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="2751",
    )

    mkdir(
        name="Ensure releases directory with setgid",
        path=paths["releases"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="2750",
    )

    mkdir(
        name="Ensure build directory (private to deploy user)",
        path=str(Path(data["project_root"]) / "build"),
        user=data["deploy_user"],
        group=data["deploy_user"],
        mode="0700",
    )

    mkdir(
        name="Ensure shared directory (owned by runtime user)",
        path=paths["shared"],
        user=data["runtime_user"],
        group=data["runtime_group"],
        mode="0711",
    )

    mkdir(
        name="Ensure placeholder release directory exists",
        path=paths["placeholder_web_root"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="0750",
    )
