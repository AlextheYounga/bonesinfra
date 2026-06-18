"""Deploy context defaults should preserve per-project identity."""

from pathlib import Path
from tempfile import TemporaryDirectory

from bonesinfra.domain.context import DeployContext


def test_runtime_identity_defaults_to_project_name():
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
[data]
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.config.host == "example.com"
    assert ctx.runtime.web_root == "public"
    assert ctx.flat_data["runtime_user"] == "lawsnipe"
    assert ctx.flat_data["runtime_group"] == "lawsnipe"
    assert ctx.ssh_user == "root"
    assert ctx.ssh_port == 22


def test_runtime_identity_respects_explicit_override():
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
[data]
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
runtime_user = "lawsnipe-web"
runtime_group = "lawsnipe-web"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.runtime.web_root == "public"
    assert ctx.flat_data["runtime_user"] == "lawsnipe-web"
    assert ctx.flat_data["runtime_group"] == "lawsnipe-web"
