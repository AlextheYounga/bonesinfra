import sys
from pathlib import Path

from pyinfra import host
from pyinfra.operations import server, systemd

from bonesinfra.infra.deploy_helpers import render
from bonesinfra.infra.utils import unflatten


def deploy_ssl():
    data = unflatten(host.data.dict())
    paths = data.get("paths", {})
    here = Path(__file__).parent.parent.parent

    if not data.get("ssl_domain") or not data.get("ssl_email"):
        print("Error: ssl_domain and ssl_email are required", file=sys.stderr)
        sys.exit(1)

    _render_router_config(data, paths, here, ssl_enabled=False, stage="certbot challenge")
    obtain_certificate(data, paths)
    _render_router_config(data, paths, here, ssl_enabled=True, stage="SSL enable")


def _render_router_config(data, paths, here, ssl_enabled, stage):
    render(
        f"Render nginx config ({stage})",
        here / "assets/nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        nginx_server_name=data["ssl_domain"],
        nginx_ssl_enabled=ssl_enabled,
        **data,
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


def obtain_certificate(data, paths):
    server.shell(
        name="Obtain or renew certificate",
        commands=[
            "certbot certonly --non-interactive --agree-tos "
            f"--email {data['ssl_email']} "
            "--webroot "
            f"-w {paths['current_web_root']} "
            f"-d {data['ssl_domain']} "
            "--keep-until-expiring"
        ],
        _sudo=True,
    )
