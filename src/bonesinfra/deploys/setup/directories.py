from pathlib import Path
from shlex import quote

from pyinfra.operations import server

from bonesinfra.infra.deploy_helpers import mkdir


def _user_env_command(user, command):
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    return f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"


def setup_repo_and_project(ctx, paths):
    mkdir(
        name="Ensure bare repo parent directory exists",
        path=paths["repo_parent"],
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
    )

    server.shell(
        name="Initialize bare git repo",
        commands=[_user_env_command(ctx.config.deploy_user, f"git init --bare {quote(paths['repo'])}")],
        _sudo=True,
        _sudo_user=ctx.config.deploy_user,
    )

    mkdir(
        name="Ensure bare repo bones directory exists",
        path=paths["repo_bones"],
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
    )

    mkdir(
        name="Ensure project root parent directory is traversable",
        path=paths["project_root_parent"],
        mode="0711",
    )

    mkdir(
        name="Ensure project root with setgid for release group",
        path=ctx.config.project_root,
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="2751",
    )

    mkdir(
        name="Ensure releases directory with setgid",
        path=paths["releases"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="2750",
    )

    mkdir(
        name="Ensure build directory (private to deploy user)",
        path=str(Path(ctx.config.project_root) / "build"),
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
        mode="0700",
    )

    mkdir(
        name="Ensure shared directory (owned by runtime user)",
        path=paths["shared"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="2775",
    )

    mkdir(
        name="Ensure placeholder release directory exists",
        path=paths["placeholder_web_root"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="0750",
    )
