from types import SimpleNamespace

from bonesinfra.deploys.dbs import services


def _ctx(service_names):
    return SimpleNamespace(
        app=SimpleNamespace(project_name="atlas-api"),
        dbs=SimpleNamespace(services=tuple(service_names)),
        paths_dict={"shared": "/srv/sites/atlas/shared"},
    )


def test_selected_services_only_schedule_selected_packages(monkeypatch):
    installed = []
    commands = []
    monkeypatch.setattr(services.apt, "packages", lambda **kwargs: installed.append(kwargs))
    monkeypatch.setattr(services.server, "shell", lambda **kwargs: commands.append(kwargs))
    monkeypatch.setattr(services.systemd, "service", lambda **kwargs: commands.append(kwargs))

    services.provision(_ctx(["postgres", "valkey"]))

    assert installed[0]["packages"] == ["postgresql", "valkey-server"]
    assert all("mysql" not in str(command) for command in commands)
    assert any("127.0.0.1" in str(command) for command in commands)


def test_database_identifier_rejects_unsafe_project_names():
    assert services._database_identifier("atlas-api") == "atlas_api"
    try:
        services._database_identifier("atlas;drop")
    except ValueError:
        pass
    else:
        raise AssertionError("unsafe database identifier was accepted")
