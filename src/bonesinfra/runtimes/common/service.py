from pathlib import Path

from pyinfra.operations import files, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.runtimes.common import validation


def runtime_paths(ctx):
    return ctx.paths_dict


def render_app_service(  # noqa: PLR0913
    ctx,
    *,
    paths,
    name,
    runtime_label,
    runtime_exec,
    apparmor_profile_name,
    runtime_write_paths,
    runtime_address_families="AF_UNIX",
):
    here = Path(__file__).parent
    project = ctx.app.project_name
    files.template(
        name=f"Deploy {name} systemd service",
        src=str(here / "assets/app.service.j2"),
        dest=f"/etc/systemd/system/{project}-{name}.service",
        user="root",
        group="root",
        mode="0644",
        runtime_name=name,
        runtime_label=runtime_label,
        runtime_exec=runtime_exec,
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=" ".join(runtime_write_paths),
        runtime_address_families=runtime_address_families,
        **template_data(ctx, paths=paths),
        _sudo=True,
    )


def enable_and_start(ctx, name, *, apparmor_profile_name=None):
    service = f"{ctx.app.project_name}-{name}.service"
    systemd.service(
        name=f"Enable and start {name} service",
        service=service,
        enabled=True,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )
    if apparmor_profile_name:
        validation.verify_profile_attached(service, apparmor_profile_name)
