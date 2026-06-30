import pytest

from bonesinfra.deploys.runtime import nginx as runtime_nginx
from bonesinfra.domain.context import DeployContext
from bonesinfra.domain.paths import DeploymentPaths


def _make_ctx(tmp_path, *, domain: str = "", preview_domain: str = "preview.example.com"):
    config_path = tmp_path / "bones.toml"
    config_path.write_text(
        f"""
project_name = "lawsnipe"
repo_path = "/srv/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
domain = "{domain}"
preview_domain = "{preview_domain}"
email = "ops@example.com"
""".lstrip()
    )
    return DeployContext.from_files(str(config_path))


def _noop(*args, **kwargs):
    del args, kwargs


def test_runtime_nginx_uses_preview_domain_when_domain_is_empty(tmp_path, monkeypatch):
    ctx = _make_ctx(tmp_path, domain="", preview_domain="preview.example.com")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    calls = []

    monkeypatch.setattr(runtime_nginx, "mkdir", _noop)
    monkeypatch.setattr(runtime_nginx.files, "link", _noop)
    monkeypatch.setattr(runtime_nginx.server, "shell", _noop)
    monkeypatch.setattr(runtime_nginx.systemd, "daemon_reload", _noop)
    monkeypatch.setattr(runtime_nginx.nginx_safety, "install_default_deny_server", _noop)
    monkeypatch.setattr(runtime_nginx.nginx_safety, "validate_config", _noop)

    def fake_render(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(runtime_nginx, "render", fake_render)

    runtime_nginx.setup(ctx, paths)

    router_call = next(call for _, call in calls if "nginx_server_name" in call)
    assert router_call["nginx_server_name"] == "preview.example.com"
    assert router_call["preview_domain"] == "preview.example.com"


def test_runtime_nginx_requires_a_real_name(tmp_path, monkeypatch):
    ctx = _make_ctx(tmp_path, domain="", preview_domain="")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__

    monkeypatch.setattr(runtime_nginx, "mkdir", _noop)
    monkeypatch.setattr(runtime_nginx.files, "link", _noop)
    monkeypatch.setattr(runtime_nginx.server, "shell", _noop)
    monkeypatch.setattr(runtime_nginx.systemd, "daemon_reload", _noop)
    monkeypatch.setattr(runtime_nginx.nginx_safety, "install_default_deny_server", _noop)
    monkeypatch.setattr(runtime_nginx.nginx_safety, "validate_config", _noop)
    monkeypatch.setattr(runtime_nginx, "render", _noop)

    with pytest.raises(ValueError, match="domain or preview_domain"):
        runtime_nginx.setup(ctx, paths)
