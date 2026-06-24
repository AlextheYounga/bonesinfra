from bonesinfra.deploys import nginx_safety


def test_validate_config_rejects_conflicting_server_name_warning(monkeypatch):
    calls = []

    def fake_shell(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(nginx_safety.server, "shell", fake_shell)

    nginx_safety.validate_config("Validate nginx configuration")

    command = calls[0][1]["commands"][0]
    assert "nginx -t" in command
    assert "conflicting server name" in command
    assert "exit 1" in command


def test_install_default_deny_server_uses_dedicated_paths_and_disables_debian_default(monkeypatch, tmp_path):
    shell_calls = []
    render_calls = []
    link_calls = []
    paths = {
        "nginx_default_deny_site_available": "/etc/nginx/sites-available/00-bonesdeploy-default-deny.conf",
        "nginx_default_deny_site_enabled": "/etc/nginx/sites-enabled/00-bonesdeploy-default-deny.conf",
        "nginx_default_deny_ssl_certificate": "/etc/ssl/certs/bonesdeploy-default-deny.crt",
        "nginx_default_deny_ssl_certificate_key": "/etc/ssl/private/bonesdeploy-default-deny.key",
        "nginx_default_site_enabled": "/etc/nginx/sites-enabled/default",
    }

    def fake_shell(*args, **kwargs):
        shell_calls.append((args, kwargs))

    def fake_render(*args, **kwargs):
        render_calls.append((args, kwargs))

    def fake_link(*args, **kwargs):
        link_calls.append((args, kwargs))

    monkeypatch.setattr(nginx_safety.server, "shell", fake_shell)
    monkeypatch.setattr(nginx_safety, "render", fake_render)
    monkeypatch.setattr(nginx_safety.files, "link", fake_link)

    nginx_safety.install_default_deny_server(paths, tmp_path)

    command = shell_calls[0][1]["commands"][0]
    assert "install -d -m 0700 /etc/ssl/private" in command
    assert "openssl req -x509" in command
    assert paths["nginx_default_deny_ssl_certificate"] in command
    assert paths["nginx_default_deny_ssl_certificate_key"] in command
    assert render_calls[0][0][1] == tmp_path / "assets/nginx/default-deny.conf.j2"
    assert render_calls[0][0][2] == paths["nginx_default_deny_site_available"]
    # default-deny server is enabled; Debian stock default site is disabled in
    # the same installer so runtime and ssl paths are independently safe.
    assert link_calls[0][1]["path"] == paths["nginx_default_deny_site_enabled"]
    assert link_calls[1][1]["path"] == paths["nginx_default_site_enabled"]
    assert link_calls[1][1]["present"] is False
