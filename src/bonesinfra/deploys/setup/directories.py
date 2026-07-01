from shlex import quote

from pyinfra.operations import files, server

from bonesinfra.domain.paths import ASSETS_DIR
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

    repo = quote(paths["repo"])
    server.shell(
        name="Set bare repo default branch",
        commands=[f"git --git-dir {repo} symbolic-ref HEAD refs/heads/{ctx.config.branch}"],
        _sudo=True,
        _sudo_user=ctx.config.deploy_user,
    )

    files.put(
        name="Install bare repo post-receive hook",
        src=str(ASSETS_DIR / "hooks/post-receive"),
        dest=f"{paths['repo']}/hooks/post-receive",
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
        mode="0755",
        _sudo=True,
    )

    mkdir(
        name="Ensure project root parent directory is traversable",
        path=paths["project_root_parent"],
        mode="0711",
    )

    mkdir(
        name="Ensure project root boundary exists",
        path=ctx.config.project_root,
        user="root",
        group="root",
        mode="0751",
    )

    mkdir(
        name="Ensure releases directory with setgid",
        path=paths["releases"],
        user="root",
        group=ctx.runtime.runtime_group,
        mode="2750",
    )

    mkdir(
        name="Ensure shared directory (owned by runtime user)",
        path=paths["shared"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0750",
    )

    mkdir(
        name="Ensure placeholder release directory exists",
        path=paths["placeholder_web_root"],
        user="root",
        group=ctx.runtime.runtime_group,
        mode="0750",
    )
