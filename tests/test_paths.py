"""Paths manifest must define `build_logs` and `LOGS_DIR` for centralized log handling."""

from bonesinfra.domain.paths import DeploymentPaths

from . import helpers

CRATES_PATHS = helpers.REPO_ROOT / "crates/shared/src/paths.rs"


def test_paths_has_build_logs_constant():
    if not CRATES_PATHS.exists():
        return
    c = helpers.read(CRATES_PATHS)
    helpers.assert_contains(c, 'pub const LOGS_DIR: &str = "logs";')
    helpers.assert_contains(c, "pub build_logs: String,")
    helpers.assert_contains(
        c,
        "build_logs: Path::new(&project_root).join(BUILD_DIR).join(LOGS_DIR).display().to_string()",
    )


def test_paths_include_global_nginx_default_deny_site():
    paths = DeploymentPaths.new("lawsnipe", "/home/git/lawsnipe.git", "/srv/sites/lawsnipe")

    assert paths.nginx_default_deny_site_available == "/etc/nginx/sites-available/00-bonesdeploy-default-deny.conf"
    assert paths.nginx_default_deny_site_enabled == "/etc/nginx/sites-enabled/00-bonesdeploy-default-deny.conf"
    assert paths.nginx_default_deny_ssl_certificate == "/etc/ssl/certs/bonesdeploy-default-deny.crt"
    assert paths.nginx_default_deny_ssl_certificate_key == "/etc/ssl/private/bonesdeploy-default-deny.key"
