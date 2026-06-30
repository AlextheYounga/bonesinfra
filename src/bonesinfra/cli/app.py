import json
import sys

import typer

from bonesinfra.deploys.helpers.plan import deploy_helpers
from bonesinfra.deploys.runtime.plan import deploy_runtime
from bonesinfra.deploys.setup.plan import deploy_setup
from bonesinfra.deploys.ssl.plan import deploy_ssl
from bonesinfra.domain.context import DeployContext
from bonesinfra.infra.pyinfra_runner import run
from bonesinfra.runtimes import get_runtime, list_runtimes

app = typer.Typer()
runtime_app = typer.Typer()
setup_app = typer.Typer()
ssl_app = typer.Typer()
helpers_app = typer.Typer()
app.add_typer(runtime_app, name="runtime", help="Runtime operations")
app.add_typer(setup_app, name="setup", help="Setup operations")
app.add_typer(ssl_app, name="ssl", help="SSL operations")
app.add_typer(helpers_app, name="helpers", help="Helper tool operations")


def _validate_host(ctx: DeployContext) -> None:
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)


@runtime_app.command("list")
def runtime_list():
    print(json.dumps(list_runtimes()))


@runtime_app.command("questions")
def runtime_questions(
    runtime: str = typer.Argument(help="Runtime name"),
):
    print(json.dumps(get_runtime(runtime).questions()))


@runtime_app.command("apply")
def runtime_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    runtime_config: str = typer.Option(..., "--runtime-config", help="Path to runtime.toml"),
):
    ctx = DeployContext.from_files(config, runtime_config)
    _validate_host(ctx)
    run(ctx=ctx, deploy=deploy_runtime)


@setup_app.command("apply")
def setup_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
):
    ctx = DeployContext.from_files(config)
    _validate_host(ctx)
    run(ctx=ctx, deploy=deploy_setup)


@ssl_app.command("apply")
def ssl_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
):
    ctx = DeployContext.from_files(config)
    if not ctx.config.domain or not ctx.config.email:
        print("Error: ssl.domain and ssl.email are required in bones.toml", file=sys.stderr)
        sys.exit(3)
    _validate_host(ctx)
    run(ctx=ctx, deploy=deploy_ssl)


@helpers_app.command("apply")
def helpers_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
):
    ctx = DeployContext.from_files(config)
    _validate_host(ctx)
    run(ctx=ctx, deploy=deploy_helpers)
