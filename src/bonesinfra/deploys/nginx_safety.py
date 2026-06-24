from pyinfra.operations import files, server

from bonesinfra.infra.deploy_helpers import render


def install_default_deny_server(paths, here):
    # ponytail: self-signed is enough here because this server never serves
    # content; it only gives nginx a TLS default that can return 444.
    server.shell(
        name="Ensure nginx default-deny SSL certificate exists",
        commands=[
            "if [ ! -s {cert} ] || [ ! -s {key} ]; then "
            "install -d -m 0755 /etc/ssl/certs && "
            "install -d -m 0700 /etc/ssl/private && "
            "openssl req -x509 -nodes -newkey rsa:2048 -days 3650 "
            "-subj /CN=bonesdeploy-default-deny.invalid "
            "-keyout {key} -out {cert} && "
            "chmod 0600 {key} && chmod 0644 {cert}; "
            "fi".format(
                cert=paths["nginx_default_deny_ssl_certificate"],
                key=paths["nginx_default_deny_ssl_certificate_key"],
            )
        ],
        _sudo=True,
    )

    render(
        "Deploy nginx default-deny server",
        here / "assets/nginx/default-deny.conf.j2",
        paths["nginx_default_deny_site_available"],
        mode="0644",
        paths=paths,
    )

    files.link(
        name="Enable nginx default-deny server",
        path=paths["nginx_default_deny_site_enabled"],
        target=paths["nginx_default_deny_site_available"],
        force=True,
        _sudo=True,
    )

    files.link(
        name="Disable Debian default nginx site",
        path=paths["nginx_default_site_enabled"],
        present=False,
        _sudo=True,
    )


def validate_config(name):
    server.shell(
        name=name,
        commands=[
            'output=$(nginx -t 2>&1); status=$?; printf "%s\\n" "$output"; '
            '[ "$status" -eq 0 ] || exit "$status"; '
            'case "$output" in *"conflicting server name"*) exit 1;; esac'
        ],
        _sudo=True,
    )
