
from pyinfra.operations import files, server, systemd


def setup(data, paths, here):
    systemd.service(
        name="Ensure apparmor service is enabled and started",
        service="apparmor",
        enabled=True,
        running=True,
        _sudo=True,
    )

    server.shell(
        name="Verify apparmor kernel enabled",
        commands=[f"cat {paths['apparmor_enabled_param']}"],
        _sudo=True,
    )

    apparmor_profile_name = f"bonesdeploy-{data['project_name']}-nginx"
    apparmor_profile_path = f"/etc/apparmor.d/{apparmor_profile_name}"

    files.template(
        name="Deploy per-project apparmor profile",
        src=str(here / "assets/apparmor/project-nginx-profile.j2"),
        dest=apparmor_profile_path,
        user="root",
        group="root",
        mode="0644",
        apparmor_profile_name=apparmor_profile_name,
        **data,
        _sudo=True,
    )

    server.shell(
        name="Load updated apparmor profile",
        commands=[f"apparmor_parser -r {apparmor_profile_path}"],
        _sudo=True,
    )

    server.shell(
        name="Ensure project profile is in enforce mode",
        commands=[f"aa-enforce {apparmor_profile_path}"],
        _sudo=True,
    )
