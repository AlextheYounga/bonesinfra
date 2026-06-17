from pathlib import Path

from pyinfra.operations import files, server


def setup_repo_and_project(data, paths):
    files.directory(
        name="Ensure bare repo parent directory exists",
        path=paths["repo_parent"],
        user=data["deploy_user"],
        group=data["deploy_user"],
        mode="0755",
        _sudo=True,
    )

    server.shell(
        name="Initialize bare git repo",
        commands=[f"git init --bare {paths['repo']}"],
        _sudo=True,
        _sudo_user=data["deploy_user"],
    )

    files.directory(
        name="Ensure bare repo bones directory exists",
        path=paths["repo_bones"],
        user=data["deploy_user"],
        group=data["deploy_user"],
        mode="0755",
        _sudo=True,
    )

    files.directory(
        name="Ensure project root parent directory is traversable",
        path=paths["project_root_parent"],
        user="root",
        group="root",
        mode="0711",
        _sudo=True,
    )

    files.directory(
        name="Ensure project root with setgid for release group",
        path=data["project_root"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="2751",
        _sudo=True,
    )

    files.directory(
        name="Ensure releases directory with setgid",
        path=paths["releases"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="2750",
        _sudo=True,
    )

    files.directory(
        name="Ensure build directory (private to deploy user)",
        path=str(Path(data["project_root"]) / "build"),
        user=data["deploy_user"],
        group=data["deploy_user"],
        mode="0700",
        _sudo=True,
    )

    files.directory(
        name="Ensure shared directory (owned by runtime user)",
        path=paths["shared"],
        user=data["runtime_user"],
        group=data["runtime_group"],
        mode="0711",
        _sudo=True,
    )

    files.directory(
        name="Ensure placeholder release directory exists",
        path=paths["placeholder_web_root"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="0750",
        _sudo=True,
    )
