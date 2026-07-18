import re
from pathlib import Path

from pyinfra.operations import files, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.runtimes.common import validation

SERVICE_NAME_RE = re.compile(r"[a-z0-9][a-z0-9_-]*")


def runtime_paths(ctx):
    return ctx.paths_dict


def render_target(ctx, *, paths):
    """Install the root-owned systemd lifecycle target for this site."""
    here = Path(__file__).parent
    files.template(
        name="Deploy site systemd target",
        src=str(here / "assets/site.target.j2"),
        dest=paths["systemd_site_target"],
        user="root",
        group="root",
        mode="0644",
        **template_data(ctx, paths=paths),
        _sudo=True,
    )
    files.directory(
        name="Remove stale site systemd target memberships",
        path=paths["systemd_site_target_requires"],
        present=False,
        _sudo=True,
    )
    files.directory(
        name="Ensure site systemd target requires directory exists",
        path=paths["systemd_site_target_requires"],
        user="root",
        group="root",
        mode="0755",
        _sudo=True,
    )


def register_service(ctx, *, paths, name):
    """Register an exact, project-derived required unit in the site's target."""
    if not SERVICE_NAME_RE.fullmatch(name):
        raise ValueError(f"invalid site service name: {name}")
    service_name = f"{ctx.app.project_name}-{name}.service"
    files.link(
        name=f"Require {service_name} from site target",
        path=f"{paths['systemd_site_target_requires']}/{service_name}",
        target=f"/etc/systemd/system/{service_name}",
        user="root",
        group="root",
        force=True,
        _sudo=True,
    )


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
    register_service(ctx, paths=paths, name=name)


def enable_and_start(ctx, name, *, apparmor_profile_name=None):
    service = f"{ctx.app.project_name}-{name}.service"
    systemd.service(
        name=f"Remove {name} service from multi-user boot and start it",
        service=service,
        enabled=False,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )
    if apparmor_profile_name:
        validation.verify_profile_attached(service, apparmor_profile_name)
