from pathlib import Path

from pyinfra.operations import files, server, systemd

from bonesinfra.infra.deploy_helpers import mkdir, render


def setup(data, paths, here):
    mkdir(
        name="Ensure socket directory exists",
        path=paths["runtime_socket_dir"],
        user=data["runtime_user"],
        group=data["runtime_group"],
        mode="0750",
    )

    mkdir(
        name="Ensure conf directory exists",
        path=paths["conf_root"],
        group=data["runtime_group"],
        mode="0750",
    )

    render(
        "Deploy per-site nginx config",
        here / "assets/nginx/site-nginx.conf.j2",
        paths["site_nginx_config"],
        group=data["runtime_group"],
        mode="0640",
        **data,
    )

    render(
        "Deploy per-site nginx systemd service",
        here / "assets/nginx/site-nginx.service.j2",
        paths["systemd_site_nginx_service"],
        mode="0644",
        **data,
    )

    systemd.daemon_reload(
        name="Reload systemd after site-nginx service change",
        _sudo=True,
    )

    nginx_server_name = data.get("ssl_domain", "_")
    nginx_ssl_enabled = bool(data.get("ssl_cert_path") and data.get("ssl_key_path"))

    render(
        "Deploy router nginx config",
        here / "assets/nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        nginx_server_name=nginx_server_name,
        nginx_ssl_enabled=nginx_ssl_enabled,
        nginx_ssl_certificate_path=data.get("ssl_cert_path", ""),
        nginx_ssl_certificate_key_path=data.get("ssl_key_path", ""),
        **data,
    )

    files.link(
        name="Enable router nginx site",
        path=paths["nginx_site_enabled"],
        target=paths["nginx_site_available"],
        force=True,
        _sudo=True,
    )

    files.link(
        name="Disable default nginx site",
        path=paths["nginx_default_site_enabled"],
        present=False,
        _sudo=True,
    )

    server.shell(
        name="Validate nginx configuration",
        commands=["nginx -t"],
        _sudo=True,
    )

    systemd.service(
        name="Ensure nginx service is enabled and started",
        service="nginx",
        enabled=True,
        running=True,
        _sudo=True,
    )

    site_name = Path(paths["systemd_site_nginx_service"]).stem
    systemd.service(
        name="Ensure per-site nginx service is enabled and started",
        service=site_name,
        enabled=True,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )
