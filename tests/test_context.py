"""Deploy context defaults should preserve per-project identity."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from bonesinfra.domain.context import DeployContext, template_data


def test_runtime_identity_defaults_to_project_name():
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

        ctx = DeployContext.from_files(str(config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.config.host == "example.com"
    assert ctx.config.ssh_user == "root"
    assert ctx.runtime.web_root == "public"
    assert ctx.runtime.runtime_user == "lawsnipe"
    assert ctx.runtime.runtime_group == "lawsnipe"
    assert ctx.ssh_port == 22

    td = template_data(ctx)
    assert td["runtime_user"] == "lawsnipe"
    assert td["runtime_group"] == "lawsnipe"
    assert "release_group" not in td


def test_runtime_identity_respects_explicit_override():
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
        runtime_config_path.write_text(
            """
runtime_user = "lawsnipe-web"
runtime_group = "lawsnipe-web"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path), str(runtime_config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.runtime.web_root == "public"
    assert ctx.runtime.runtime_user == "lawsnipe-web"
    assert ctx.runtime.runtime_group == "lawsnipe-web"


def test_branch_in_template_data():
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
project_name = "lawsnipe"
repo_path = "/srv/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
branch = "main"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path))

    td = template_data(ctx)
    assert td["branch"] == "main"


@pytest.mark.parametrize(
    ("runtime_toml", "message"),
    [
        ('[shared]\npaths = ".env"\n', "must be a list"),
        (
            '[shared]\npaths = [{ path = "/etc/passwd", type = "file" }]\n',
            "path must be relative",
        ),
        (
            '[shared]\npaths = [{ path = "../secrets", type = "dir" }]\n',
            "normal components only",
        ),
        (
            '[shared]\npaths = [{ path = "foo/./bar", type = "dir" }]\n',
            "normal components only",
        ),
        (
            '[shared]\npaths = [{ path = "foo/../bar", type = "dir" }]\n',
            "normal components only",
        ),
        (
            '[shared]\npaths = [{ path = "database.sqlite", type = "socket" }]\n',
            "invalid shared path type",
        ),
    ],
)
def test_invalid_shared_paths_are_rejected(runtime_toml, message):
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

        with pytest.raises((TypeError, ValueError), match=message):
            DeployContext.from_files(str(config_path), str(runtime_config_path))
