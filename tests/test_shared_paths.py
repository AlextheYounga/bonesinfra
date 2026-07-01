from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from bonesinfra.deploys.runtime import shared_paths
from bonesinfra.domain.context import DeployContext

from . import helpers

SETUP_DIRECTORIES = helpers.SRC_DIR / "bonesinfra/deploys/setup/directories.py"
SETUP_USERS = helpers.SRC_DIR / "bonesinfra/deploys/setup/users.py"
RUNTIME_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/runtime/plan.py"


def test_shared_root_is_created_with_mode_0750():
    c = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c, 'path=paths["shared"]')
    helpers.assert_contains(c, 'mode="0750"')


def test_deploy_user_is_not_added_to_runtime_group():
    c = helpers.read(SETUP_USERS)
    helpers.assert_not_contains(c, "_ensure_group_membership(ctx.config.deploy_user, ctx.runtime.runtime_group)")


def test_runtime_plan_provisions_shared_paths_before_runtime_template():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_ordering(c, "nginx.setup", "shared_paths.ensure", "template_runtime.load")


@pytest.mark.parametrize("template", ["vue", "next", "nuxt"])
def test_runtime_without_shared_paths_provisions_no_shared_leaves(template, monkeypatch):
    ctx = _make_context(f'template = "{template}"\n')
    commands = _capture_commands(ctx, monkeypatch)

    assert ctx.runtime.shared_paths == []
    assert commands == []


def test_sveltekit_provisions_blank_dotenv(monkeypatch):
    ctx = _make_context(
        """
template = "sveltekit"

[shared]
paths = [{ path = ".env", type = "file" }]
""".lstrip()
    )

    commands = _capture_commands(ctx, monkeypatch)

    assert [(path.path, path.type) for path in ctx.runtime.shared_paths] == [(".env", "file")]
    assert len(commands) == 1
    assert commands[0]["name"] == "Ensure shared file .env"
    assert "touch /srv/sites/lawsnipe/shared/.env" in commands[0]["commands"][0]
    assert "chown root:lawsnipe /srv/sites/lawsnipe/shared/.env" in commands[0]["commands"][0]
    assert "chmod 0640 /srv/sites/lawsnipe/shared/.env" in commands[0]["commands"][0]


def test_rails_provisions_declared_shared_leaves(monkeypatch):
    ctx = _make_context(
        """
template = "rails"

[shared]
paths = [
  { path = ".env", type = "file" },
  { path = "tmp", type = "dir" },
  { path = "log", type = "dir" },
  { path = "storage", type = "dir" },
]
""".lstrip()
    )

    commands = _capture_commands(ctx, monkeypatch)

    assert [(path.path, path.type) for path in ctx.runtime.shared_paths] == [
        (".env", "file"),
        ("tmp", "dir"),
        ("log", "dir"),
        ("storage", "dir"),
    ]
    assert [command["name"] for command in commands] == [
        "Ensure shared file .env",
        "Ensure shared directory tmp",
        "Ensure shared directory log",
        "Ensure shared directory storage",
    ]


def test_django_provisions_declared_shared_leaves(monkeypatch):
    ctx = _make_context(
        """
template = "django"

[shared]
paths = [
  { path = ".env", type = "file" },
  { path = "staticfiles", type = "dir" },
  { path = "media", type = "dir" },
]
""".lstrip()
    )

    commands = _capture_commands(ctx, monkeypatch)

    assert [(path.path, path.type) for path in ctx.runtime.shared_paths] == [
        (".env", "file"),
        ("staticfiles", "dir"),
        ("media", "dir"),
    ]
    assert [command["name"] for command in commands] == [
        "Ensure shared file .env",
        "Ensure shared directory staticfiles",
        "Ensure shared directory media",
    ]


def _make_context(runtime_toml: str) -> DeployContext:
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
project_name = "lawsnipe"
repo_path = "/srv/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
""".lstrip()
        )
        runtime_config_path = Path(tmp) / "runtime.toml"
        runtime_config_path.write_text(runtime_toml)
        return DeployContext.from_files(str(config_path), str(runtime_config_path))


def _capture_commands(ctx: DeployContext, monkeypatch):
    captured = []

    def fake_shell(*, name, commands: list[str], _sudo):
        captured.append({"name": name, "commands": commands, "sudo": _sudo})

    monkeypatch.setattr(shared_paths.server, "shell", fake_shell)
    shared_paths.ensure(ctx, ctx.paths_dict)
    return captured
