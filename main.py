#!/usr/bin/env python3
"""BonesDeploy infra CLI."""

import json
import sys
from pathlib import Path

import typer

sys.path.insert(0, str(Path(__file__).parent))

from src.runtimes import get_runtime, list_runtimes

app = typer.Typer()
runtime_app = typer.Typer()
setup_app = typer.Typer()
ssl_app = typer.Typer()
app.add_typer(runtime_app, name="runtime", help="Runtime operations")
app.add_typer(setup_app, name="setup", help="Setup operations")
app.add_typer(ssl_app, name="ssl", help="SSL operations")


@runtime_app.command("list")
def runtime_list():
    """List available runtimes."""
    print(json.dumps(list_runtimes()))


@runtime_app.command("questions")
def runtime_questions(
    runtime: str = typer.Argument(help="Runtime name"),
):
    """Get runtime questions."""
    module = get_runtime(runtime)
    questions = module.questions() if hasattr(module, "questions") else []
    print(json.dumps(questions))


def _load_deploy_config(config_path, runtime_config_path, ssh_user):
    from src.paths import DeploymentPaths
    from src.utils import load_toml

    bones_cfg = load_toml(config_path)
    data = bones_cfg.get("data", {})
    project_name = data.get("project_name", "")
    repo_path = data.get("repo_path", "")
    project_root = data.get("project_root", "")
    web_root = data.get("web_root", "public")
    host = data.get("host", "")
    port = int(data.get("port", 22))
    runtime_cfg = {}

    if runtime_config_path:
        rpath = Path(runtime_config_path)
        if rpath.exists():
            runtime_cfg = load_toml(str(rpath))

    paths = DeploymentPaths.new(project_name, repo_path, project_root, web_root)

    flat_data = {}
    flat_data["project_name"] = project_name
    flat_data["project_root"] = project_root
    flat_data["web_root"] = web_root
    flat_data["repo_path"] = repo_path
    flat_data["deploy_user"] = data.get("deploy_user", "git")
    flat_data["runtime_user"] = data.get("runtime_user", "www-data")
    flat_data["runtime_group"] = data.get("runtime_group", "www-data")
    flat_data["release_group"] = data.get("release_group", "deployers")
    flat_data["project_root_parent"] = paths.project_root_parent
    flat_data["ssh_port"] = str(port)
    flat_data["paths"] = paths.__dict__

    for key, value in runtime_cfg.items():
        if key not in flat_data:
            flat_data[key] = value

    ssl_cfg = bones_cfg.get("ssl", {})
    flat_data["ssl_domain"] = ssl_cfg.get("domain", "")
    flat_data["ssl_email"] = ssl_cfg.get("email", "")

    return host, ssh_user, port, flat_data


@runtime_app.command("apply")
def runtime_apply(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    runtime_config: str = typer.Option(..., "--runtime-config", help="Path to runtime.toml"),
    ssh_user: str = typer.Option(..., "--ssh-user", help="SSH user for remote connection"),
):
    """Apply runtime configuration."""
    host, ssh_user, port, flat_data = _load_deploy_config(config, runtime_config, ssh_user)

    if not host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        raise typer.Exit(3)

    from src.pyinfra_runner import run as run_deploy
    from src.runtime import deploy

    run_deploy(
        hostname=host,
        ssh_user=ssh_user,
        ssh_port=port,
        data=flat_data,
        deploy=deploy,
    )


@setup_app.command("apply")
def setup_apply(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    ssh_user: str = typer.Option("root", "--ssh-user", help="SSH user for remote connection"),
):
    """Apply setup configuration."""
    host, ssh_user, port, flat_data = _load_deploy_config(config, None, ssh_user)

    if not host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        raise typer.Exit(3)

    from src.pyinfra_runner import run as run_deploy
    from src.setup import deploy

    run_deploy(
        hostname=host,
        ssh_user=ssh_user,
        ssh_port=port,
        data=flat_data,
        deploy=deploy,
    )


@ssl_app.command("apply")
def ssl_apply(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    ssh_user: str = typer.Option("root", "--ssh-user", help="SSH user for remote connection"),
):
    """Apply SSL configuration."""
    host, ssh_user, port, flat_data = _load_deploy_config(config, None, ssh_user)

    if not host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        raise typer.Exit(3)

    ssl_domain = flat_data.get("ssl_domain")
    ssl_email = flat_data.get("ssl_email")
    if not ssl_domain:
        print("Error: ssl.domain is required in bones.toml", file=sys.stderr)
        raise typer.Exit(3)
    if not ssl_email:
        print("Error: ssl.email is required in bones.toml", file=sys.stderr)
        raise typer.Exit(3)

    from src.pyinfra_runner import run as run_deploy
    from src.ssl import deploy

    run_deploy(
        hostname=host,
        ssh_user=ssh_user,
        ssh_port=port,
        data=flat_data,
        deploy=deploy,
    )


def main():
    app()


if __name__ == "__main__":
    main()
