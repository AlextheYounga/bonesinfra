"""Deploy context parsing for the single bones.toml contract."""

from pathlib import Path

from bonesinfra.domain.context import DeployContext, template_data


def _write_config(tmp_path: Path, extra: str = "") -> Path:
    path = tmp_path / "bones.toml"
    path.write_text(
        f"""[app]
project_name = "lawsnipe"
remote_name = "production"

[app.server]
host = "example.com"
port = "2222"

[app.dns]
domain = "example.com"
preview_domain = "preview.example.com"
email = "ops@example.com"
ssl_enabled = true

[app.deploy]
branch = "main"
releases = 7

[build]
vars = ["PUBLIC_URL"]

[build.resources]
cpu_quota_percent = 50
memory_high_percent = 70
memory_max_percent = 90

[runtime]
runtime_user = "lawsnipe-web"
runtime_group = "lawsnipe-web"
release_group = "ignored"
{extra}"""
    )
    return path


def test_reads_nested_single_file_config(tmp_path):
    ctx = DeployContext.from_files(str(_write_config(tmp_path)))

    assert ctx.app.project_name == "lawsnipe"
    assert ctx.app.server.host == "example.com"
    assert ctx.app.server.port == "2222"
    assert ctx.paths.repo == "/srv/git/lawsnipe.git"
    assert ctx.paths.project_root == "/srv/sites/lawsnipe"
    assert ctx.app.deploy.branch == "main"
    assert ctx.app.deploy.releases == 7
    assert ctx.app.dns.ssl_enabled is True
    assert ctx.build.vars == ["PUBLIC_URL"]
    assert ctx.runtime.runtime_user == "lawsnipe-web"
    assert ctx.runtime.runtime_group == "lawsnipe-web"


def test_build_resources_are_configurable(tmp_path):
    ctx = DeployContext.from_files(str(_write_config(tmp_path)))
    assert ctx.build.resources.cpu_quota_percent == 50
    assert ctx.build.resources.memory_high_percent == 70
    assert ctx.build.resources.memory_max_percent == 90


def test_template_data_contains_runtime_values(tmp_path):
    td = template_data(DeployContext.from_files(str(_write_config(tmp_path))))
    assert td["runtime_user"] == "lawsnipe-web"
    assert td["runtime_group"] == "lawsnipe-web"
    assert "release_group" not in td


def test_missing_nested_tables_use_defaults(tmp_path):
    path = tmp_path / "bones.toml"
    path.write_text('[app]\nproject_name = "lawsnipe"\n')
    ctx = DeployContext.from_files(str(path))
    assert ctx.app.deploy.branch == "master"
    assert ctx.app.server.host == ""
    assert ctx.runtime.runtime_user == "lawsnipe"
