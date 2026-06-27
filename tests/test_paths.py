"""Deployment paths should match the v1 host layout."""

from bonesinfra.domain.paths import DeploymentPaths


def test_paths_default_repo_parent_is_srv_git():
    paths = DeploymentPaths.new("lawsnipe", "/srv/git/lawsnipe.git", "/srv/sites/lawsnipe")

    assert paths.repo_parent == "/srv/git"


def test_paths_do_not_include_permanent_build_paths():
    paths = DeploymentPaths.new("lawsnipe", "/srv/git/lawsnipe.git", "/srv/sites/lawsnipe")

    assert not hasattr(paths, "build_root")
    assert not hasattr(paths, "build_logs")


def test_paths_include_site_registry_path():
    paths = DeploymentPaths.new("lawsnipe", "/srv/git/lawsnipe.git", "/srv/sites/lawsnipe")

    assert paths.site_registry_path == "/etc/bonesdeploy/sites/lawsnipe.toml"


def test_paths_include_global_nginx_default_deny_site():
    paths = DeploymentPaths.new("lawsnipe", "/srv/git/lawsnipe.git", "/srv/sites/lawsnipe")

    assert paths.nginx_default_deny_site_available == "/etc/nginx/sites-available/00-bonesdeploy-default-deny.conf"
    assert paths.nginx_default_deny_site_enabled == "/etc/nginx/sites-enabled/00-bonesdeploy-default-deny.conf"
    assert paths.nginx_default_deny_ssl_certificate == "/etc/ssl/certs/bonesdeploy-default-deny.crt"
    assert paths.nginx_default_deny_ssl_certificate_key == "/etc/ssl/private/bonesdeploy-default-deny.key"
