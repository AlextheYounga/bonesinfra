from types import SimpleNamespace

import pytest

from bonesinfra.runtimes.common import service


def test_register_service_uses_exact_project_derived_unit(monkeypatch):
    calls = []
    monkeypatch.setattr(service.files, "link", lambda **kwargs: calls.append(kwargs))
    ctx = SimpleNamespace(app=SimpleNamespace(project_name="shop"))
    paths = {"systemd_site_target_requires": "/etc/systemd/system/shop.target.requires"}

    service.register_service(ctx, paths=paths, name="nginx")

    assert calls[0]["path"] == "/etc/systemd/system/shop.target.requires/shop-nginx.service"
    assert calls[0]["target"] == "/etc/systemd/system/shop-nginx.service"
    assert calls[0]["target"] != "/etc/systemd/system/shop-admin-nginx.service"


def test_register_service_rejects_arbitrary_unit_suffix(monkeypatch):
    def ignore_link(*_args, **_kwargs):
        return None

    monkeypatch.setattr(service.files, "link", ignore_link)
    ctx = SimpleNamespace(app=SimpleNamespace(project_name="shop"))
    paths = {"systemd_site_target_requires": "/etc/systemd/system/shop.target.requires"}

    with pytest.raises(ValueError, match="invalid site service name"):
        service.register_service(ctx, paths=paths, name="admin.service")

    with pytest.raises(ValueError, match="invalid site service name"):
        service.register_service(ctx, paths=paths, name="-admin")


def test_render_target_reconciles_stale_memberships(monkeypatch):
    def ignore_template(*_args, **_kwargs):
        return None

    def empty_template_data(*_args, **_kwargs):
        return {}

    directory_calls = []
    monkeypatch.setattr(service.files, "template", ignore_template)
    monkeypatch.setattr(service.files, "directory", lambda **kwargs: directory_calls.append(kwargs))
    monkeypatch.setattr(service, "template_data", empty_template_data)
    ctx = SimpleNamespace(app=SimpleNamespace(project_name="shop"))
    paths = {
        "systemd_site_target": "/etc/systemd/system/shop.target",
        "systemd_site_target_requires": "/etc/systemd/system/shop.target.requires",
    }

    service.render_target(ctx, paths=paths)

    assert directory_calls == [
        {
            "name": "Remove stale site systemd target memberships",
            "path": "/etc/systemd/system/shop.target.requires",
            "present": False,
            "_sudo": True,
        },
        {
            "name": "Ensure site systemd target requires directory exists",
            "path": "/etc/systemd/system/shop.target.requires",
            "user": "root",
            "group": "root",
            "mode": "0755",
            "_sudo": True,
        },
    ]


def test_enable_and_start_removes_legacy_direct_service_enablement(monkeypatch):
    calls = []
    monkeypatch.setattr(service.systemd, "service", lambda **kwargs: calls.append(kwargs))
    ctx = SimpleNamespace(app=SimpleNamespace(project_name="shop"))

    service.enable_and_start(ctx, "next")

    assert {"service": "shop-next.service", "enabled": False, "running": True}.items() <= calls[0].items()
