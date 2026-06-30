from pathlib import Path

from pyinfra.operations import files, server, systemd

from bonesinfra.deploys._shared import nginx_safety
from bonesinfra.domain.context import template_data
from bonesinfra.domain.paths import ASSETS_DIR
from bonesinfra.infra.deploy_helpers import letsencrypt_cert_paths, mkdir, render


def setup(ctx, paths):
    # 0711: system nginx (www-data) needs traversal to reach the per-site
    # nginx socket at /run/<project>/nginx/nginx.sock. 0750 would block it.
    mkdir(
        name="Ensure socket directory exists",
        path=paths["runtime_socket_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
    )

    mkdir(
        name="Ensure nginx runtime directory exists",
        path=paths["runtime_nginx_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
    )

    mkdir(
        name="Ensure conf directory exists",
        path=paths["conf_root"],
        group=ctx.runtime.runtime_group,
        mode="0750",
    )

    render(
        "Deploy per-site nginx config",
        ASSETS_DIR / "nginx/site-nginx.conf.j2",
        paths["site_nginx_config"],
        group=ctx.runtime.runtime_group,
        mode="0640",
        **template_data(ctx, paths=paths),
    )

    render(
        "Deploy per-site nginx systemd service",
        ASSETS_DIR / "nginx/site-nginx.service.j2",
        paths["systemd_site_nginx_service"],
        mode="0644",
        **template_data(ctx, paths=paths),
    )

    systemd.daemon_reload(
        name="Reload systemd after site-nginx service change",
        _sudo=True,
    )

    nginx_server_name = ctx.config.domain or ctx.config.preview_domain
    if not nginx_server_name:
        raise ValueError("domain or preview_domain is required for nginx config")

    # SSL state comes from bones.toml (ssl_enabled), not runtime.toml — SSL is
    # owned by `ssl apply`, not `runtime apply`. This keeps runtime apply from
    # clobbering the SSL router config that ssl apply wrote.
    nginx_ssl_enabled = ctx.config.ssl_enabled and ctx.config.domain
    cert_path, key_path = letsencrypt_cert_paths(ctx.config.domain or nginx_server_name)

    render(
        "Deploy router nginx config",
        ASSETS_DIR / "nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        nginx_server_name=nginx_server_name,
        nginx_ssl_enabled=nginx_ssl_enabled,
        nginx_ssl_certificate_path=cert_path,
        nginx_ssl_certificate_key_path=key_path,
        **template_data(ctx, paths=paths),
    )

    nginx_safety.install_default_deny_server(paths)

    files.link(
        name="Enable router nginx site",
        path=paths["nginx_site_enabled"],
        target=paths["nginx_site_available"],
        force=True,
        _sudo=True,
    )

    nginx_safety.validate_config("Validate nginx configuration")


def start_services(paths):
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

    # ponytail: reload only after the per-site nginx socket exists, so the
    # router never flips over to a missing upstream and briefly serves 502s.
    server.shell(
        name="Reload nginx to apply site config changes",
        commands=["systemctl reload nginx"],
        _sudo=True,
    )
