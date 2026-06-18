from pyinfra.operations import files, server

from bonesinfra.domain.context import template_data


def setup_php_fpm(ctx, here):
    project = ctx.config.project_name
    profile_name = f"bonesdeploy-{project}-php-fpm"
    profile_path = f"/etc/apparmor.d/{profile_name}"

    files.template(
        name="Deploy PHP-FPM AppArmor profile",
        src=str(here / "assets/php/site-php-fpm-profile.j2"),
        dest=profile_path,
        user="root",
        group="root",
        mode="0644",
        apparmor_profile_name=profile_name,
        **template_data(ctx),
        _sudo=True,
    )

    server.shell(
        name="Load PHP-FPM AppArmor profile",
        commands=[f"apparmor_parser -r -T -W {profile_path}"],
        _sudo=True,
    )
