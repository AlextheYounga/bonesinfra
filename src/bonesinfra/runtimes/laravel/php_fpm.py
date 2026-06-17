from pyinfra.operations import files, server, systemd


def setup_storage_directories(paths, data):
    runtime_user = data["runtime_user"]
    runtime_group = data["runtime_group"]
    subdirs = ["logs", "framework/cache", "framework/sessions", "framework/views"]
    for subdir in subdirs:
        files.directory(
            name=f"Ensure storage/{subdir} exists",
            path=f"{paths['current']}/storage/{subdir}",
            user=runtime_user,
            group=runtime_group,
            mode="0775",
            _sudo=True,
        )


def setup_pool(here, data, paths, php_version):
    project = data["project_name"]
    runtime_group = data["runtime_group"]
    pool_config_path = f"/srv/conf/{project}/php-fpm.conf"
    php_fpm_socket_path = paths["runtime_php_fpm_socket"]

    files.directory(
        name="Ensure conf directory exists",
        path=paths["conf_root"],
        user="root",
        group=runtime_group,
        mode="0750",
        _sudo=True,
    )

    files.template(
        name="Deploy PHP-FPM pool config",
        src=str(here / "assets/php/php-fpm-pool.conf.j2"),
        dest=pool_config_path,
        user="root",
        group="root",
        mode="0644",
        laravel_php_fpm_pool_name=project,
        laravel_php_fpm_socket_path=php_fpm_socket_path,
        **data,
        _sudo=True,
    )

    files.template(
        name="Deploy PHP-FPM systemd service",
        src=str(here / "assets/php/site-php-fpm.service.j2"),
        dest=f"/etc/systemd/system/{project}-php-fpm.service",
        user="root",
        group="root",
        mode="0644",
        laravel_php_fpm_pool_config_path=pool_config_path,
        laravel_php_version_resolved=php_version,
        apparmor_profile_name=f"bonesdeploy-{project}-php-fpm",
        **data,
        _sudo=True,
    )

    server.shell(
        name="Validate PHP-FPM configuration",
        commands=[f"/usr/sbin/php-fpm{php_version} --test --fpm-config {pool_config_path}"],
        _sudo=True,
    )

    systemd.service(
        name="Enable and start per-project PHP-FPM service",
        service=f"{project}-php-fpm.service",
        enabled=True,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )
