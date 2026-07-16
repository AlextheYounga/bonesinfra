"""The single-file runtime contract no longer has a shared-path table."""

from bonesinfra.domain.context import DeployContext


def test_runtime_permissions_match_bones_toml_shape(tmp_path):
    path = tmp_path / "bones.toml"
    path.write_text(
        """[app]
project_name = "lawsnipe"

[runtime.permissions]
paths = [{ path = "*", type = "dir", mode = "750" }]
"""
    )
    ctx = DeployContext.from_files(str(path))
    assert ctx.runtime.permissions.paths[0]["mode"] == "750"
