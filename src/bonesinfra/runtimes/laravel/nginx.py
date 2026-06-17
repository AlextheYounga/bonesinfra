from pyinfra.operations import files, server, systemd


def setup(here, data, paths):
    project = data["project_name"]
    runtime_user = data["runtime_user"]
    runtime_group = data["runtime_group"]
    php_fpm_socket_path = paths["runtime_php_fpm_socket"]

    files.template(
        name="Deploy Laravel-specific per-site nginx config",
        src=str(here / "assets/nginx/laravel-site-nginx.conf.j2"),
        dest=paths["site_nginx_config"],
        user="root",
        group=runtime_group,
        mode="0640",
        laravel_php_fpm_socket_path=php_fpm_socket_path,
        **data,
        _sudo=True,
    )

    files.directory(
        name="Ensure runtime socket directory exists before nginx validation",
        path=paths["runtime_socket_dir"],
        user=runtime_user,
        group=runtime_group,
        mode="0750",
        _sudo=True,
    )

    server.shell(
        name="Validate nginx configuration with Laravel config",
        commands=[f"nginx -t -c {paths['site_nginx_config']}"],
        _sudo=True,
    )

    systemd.service(
        name="Restart per-site nginx with Laravel config",
        service=f"{project}-nginx",
        restarted=True,
        _sudo=True,
    )
