from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.toml_store import load_toml


DEPLOY_USER = "git"

DEFAULT_SSH_USER = "root"
DEFAULT_SSH_PORT = "22"
DEFAULT_WEB_ROOT = "public"


@dataclass
class DeployContext:
    config: BonesConfig
    runtime: RuntimeConfig

    @classmethod
    def from_files(
        cls,
        config_path: str,
        runtime_config_path: str | None = None,
    ) -> DeployContext:
        bones_cfg = load_toml(config_path)
        project_name = bones_cfg.get("project_name", "")
        repo_path = bones_cfg.get("repo_path", "")
        project_root = bones_cfg.get("project_root", "")
        host = bones_cfg.get("host", "")
        port = int(bones_cfg.get("port", DEFAULT_SSH_PORT))

        runtime_cfg = {}
        if runtime_config_path:
            rpath = Path(runtime_config_path)
            if rpath.exists():
                runtime_cfg = load_toml(str(rpath))

        config = BonesConfig(
            remote_name=bones_cfg.get("remote_name", ""),
            project_name=project_name,
            ssh_user=bones_cfg.get("ssh_user", DEFAULT_SSH_USER),
            host=host,
            port=str(port),
            repo_path=repo_path,
            project_root=project_root,
            branch=bones_cfg.get("branch", ""),
            preview_domain=bones_cfg.get("preview_domain", ""),
            releases_keep=int(bones_cfg.get("releases_keep", 5)),
            ssl_enabled=bones_cfg.get("ssl_enabled", False),
            domain=bones_cfg.get("domain", ""),
            email=bones_cfg.get("email", ""),
            deploy_user=DEPLOY_USER,
        )

        runtime = RuntimeConfig(
            web_root=runtime_cfg.get("web_root", DEFAULT_WEB_ROOT),
            runtime_user=runtime_cfg.get("runtime_user", project_name),
            runtime_group=runtime_cfg.get("runtime_user", project_name),
            release_group=runtime_cfg.get("runtime_user", f"{project_name}-release"),
            runtime_data=runtime_cfg,
        )

        return cls(config=config, runtime=runtime)

    @property
    def host(self) -> str:
        return self.config.host

    @property
    def ssh_port(self) -> int:
        return int(self.config.port)

    @property
    def deploy_data(self) -> dict[str, Any]:
        """Data dict for pyinfra host.data, assembled from structured config."""
        paths = DeploymentPaths.new(
            self.config.project_name,
            self.config.repo_path,
            self.config.project_root,
            self.runtime.web_root,
        )

        data: dict[str, Any] = {}
        data["project_name"] = self.config.project_name
        data["project_root"] = self.config.project_root
        data["web_root"] = self.runtime.web_root
        data["repo_path"] = self.config.repo_path
        data["deploy_user"] = self.config.deploy_user
        data["runtime_user"] = self.config.runtime_user
        data["runtime_group"] = self.config.runtime_group
        data["release_group"] = self.config.release_group
        data["project_root_parent"] = paths.project_root_parent
        data["ssh_port"] = int(self.config.port)
        data["paths"] = paths.__dict__
        data["ssl_domain"] = self.config.domain
        data["ssl_email"] = self.config.email

        for key, value in self.runtime.runtime_data.items():
            if key not in data:
                data[key] = value

        return data


@dataclass
class BonesConfig:
    remote_name: str
    project_name: str
    ssh_user: str
    host: str
    port: str
    repo_path: str
    project_root: str
    branch: str
    preview_domain: str
    releases_keep: int
    ssl_enabled: bool
    domain: str
    email: str
    deploy_user: str


@dataclass
class RuntimeConfig:
    web_root: str
    runtime_user: str
    runtime_group: str
    release_group: str
    runtime_data: dict[str, Any] = field(default_factory=dict)
