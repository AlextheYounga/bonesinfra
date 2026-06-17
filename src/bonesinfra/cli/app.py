import json

import typer

from bonesinfra.app import runtime_apply, runtime_catalog, setup_apply, ssl_apply

app = typer.Typer()
runtime_app = typer.Typer()
setup_app = typer.Typer()
ssl_app = typer.Typer()
app.add_typer(runtime_app, name="runtime", help="Runtime operations")
app.add_typer(setup_app, name="setup", help="Setup operations")
app.add_typer(ssl_app, name="ssl", help="SSL operations")


@runtime_app.command("list")
def runtime_list():
    print(json.dumps(runtime_catalog.list_all()))


@runtime_app.command("questions")
def runtime_questions(
    runtime: str = typer.Argument(help="Runtime name"),
):
    print(json.dumps(runtime_catalog.get_questions(runtime)))


@runtime_app.command("apply")
def runtime_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    runtime_config: str = typer.Option(..., "--runtime-config", help="Path to runtime.toml"),
    ssh_user: str = typer.Option(..., "--ssh-user", help="SSH user for remote connection"),
):
    runtime_apply.apply(config, runtime_config, ssh_user)


@setup_app.command("apply")
def setup_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    ssh_user: str = typer.Option("root", "--ssh-user", help="SSH user for remote connection"),
):
    setup_apply.apply(config, ssh_user)


@ssl_app.command("apply")
def ssl_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    ssh_user: str = typer.Option("root", "--ssh-user", help="SSH user for remote connection"),
):
    ssl_apply.apply(config, ssh_user)
