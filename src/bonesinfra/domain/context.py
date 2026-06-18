from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.toml_store import load_toml


@dataclass
class DeployContext:
    host: str
    ssh_user: str
    ssh_port: int
    flat_data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_files(
        cls,
        config_path: str,
        runtime_config_path: str | None = None,
        ssh_user: str = "root",
    ) -> DeployContext:
        bones_cfg = load_toml(config_path)
        data = bones_cfg.get("data", {})
        project_name = data.get("project_name", "")
        repo_path = data.get("repo_path", "")
        project_root = data.get("project_root", "")
        web_root = data.get("web_root", "public")
        host = data.get("host", "")
        port = int(data.get("port", 22))

        runtime_cfg = {}
        if runtime_config_path:
            rpath = Path(runtime_config_path)
            if rpath.exists():
                runtime_cfg = load_toml(str(rpath))

        paths = DeploymentPaths.new(project_name, repo_path, project_root, web_root)

        flat_data: dict[str, Any] = {}
        flat_data["project_name"] = project_name
        flat_data["project_root"] = project_root
        flat_data["web_root"] = web_root
        flat_data["repo_path"] = repo_path
        flat_data["deploy_user"] = data.get("deploy_user", "git")
        runtime_identity = project_name or "www-data"
        flat_data["runtime_user"] = data.get("runtime_user", runtime_identity)
        flat_data["runtime_group"] = data.get("runtime_group", runtime_identity)
        flat_data["release_group"] = data.get("release_group", "deployers")
        flat_data["project_root_parent"] = paths.project_root_parent
        flat_data["ssh_port"] = port
        flat_data["paths"] = paths.__dict__

        for key, value in runtime_cfg.items():
            if key not in flat_data:
                flat_data[key] = value

        ssl_cfg = bones_cfg.get("ssl", {})
        flat_data["ssl_domain"] = ssl_cfg.get("domain", "")
        flat_data["ssl_email"] = ssl_cfg.get("email", "")

        return cls(host=host, ssh_user=ssh_user, ssh_port=port, flat_data=flat_data)
