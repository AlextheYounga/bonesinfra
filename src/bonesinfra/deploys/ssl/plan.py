import sys
from pathlib import Path

from pyinfra.operations import server, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.deploy_helpers import letsencrypt_cert_paths, mkdir, render


def deploy_ssl(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent

    if not ctx.config.domain or not ctx.config.email:
        print("Error: ssl_domain and ssl_email are required", file=sys.stderr)
        sys.exit(1)

    # Dedicated, www-data-traversable webroot so the ACME challenge never
    # depends on the release tree's permissions (SSL is separate from runtime).
    mkdir(
        name="Ensure ACME webroot exists",
        path=paths["acme_webroot"],
        mode="0755",
    )

    _render_router_config(ctx, paths, here, ssl_enabled=False, stage="certbot challenge")
    obtain_certificate(ctx, paths)
    _render_router_config(ctx, paths, here, ssl_enabled=True, stage="SSL enable")


def _render_router_config(ctx, paths, here, ssl_enabled, stage):
    nginx_server_name = ctx.config.domain
    if not nginx_server_name:
        raise ValueError("domain is required for ssl nginx config")

    extra = {
        "nginx_server_name": nginx_server_name,
        "nginx_ssl_enabled": ssl_enabled,
    }
    if ssl_enabled:
        cert_path, key_path = letsencrypt_cert_paths(nginx_server_name)
        extra["nginx_ssl_certificate_path"] = cert_path
        extra["nginx_ssl_certificate_key_path"] = key_path

    render(
        f"Render nginx config ({stage})",
        here / "assets/nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        **extra,
        **template_data(ctx, paths=paths),
    )

    server.shell(
        name=f"Validate nginx configuration ({stage})",
        commands=["nginx -t"],
        _sudo=True,
    )

    systemd.service(
        name=f"Reload nginx ({stage})",
        service="nginx",
        reloaded=True,
        _sudo=True,
    )


def obtain_certificate(ctx, paths):
    server.shell(
        name="Obtain or renew certificate",
        commands=[
            "certbot certonly --non-interactive --agree-tos "
            f"--email {ctx.config.email} "
            f"--webroot "
            f"-w {paths['acme_webroot']} "
            f"-d {ctx.config.domain} "
            "--keep-until-expiring"
        ],
        _sudo=True,
    )
