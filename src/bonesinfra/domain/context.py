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
            runtime_group=runtime_cfg.get("runtime_group", project_name),
            runtime_data=runtime_cfg,
        )

        return cls(config=config, runtime=runtime)

    @property
    def host(self) -> str:
        return self.config.host

    @property
    def ssh_port(self) -> int:
        return int(self.config.port)


def template_data(ctx: DeployContext, *, paths: dict[str, Any] | None = None, **extra: Any) -> dict[str, Any]:
    """Build flat template context from DeployContext for Jinja2 template rendering."""
    if paths is None:
        p = DeploymentPaths.new(
            ctx.config.project_name, ctx.config.repo_path, ctx.config.project_root, ctx.runtime.web_root
        )
        paths = p.__dict__

    data: dict[str, Any] = {
        "project_name": ctx.config.project_name,
        "project_root": ctx.config.project_root,
        "web_root": ctx.runtime.web_root,
        "repo_path": ctx.config.repo_path,
        "deploy_user": ctx.config.deploy_user,
        "runtime_user": ctx.runtime.runtime_user,
        "runtime_group": ctx.runtime.runtime_group,
        "project_root_parent": paths["project_root_parent"],
        "ssh_port": int(ctx.config.port),
        "paths": paths,
        "ssl_domain": ctx.config.domain,
        "ssl_email": ctx.config.email,
        "preview_domain": ctx.config.preview_domain,
    }

    for key, value in ctx.runtime.runtime_data.items():
        if key not in data:
            data[key] = value

    data.update(extra)
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
    runtime_data: dict[str, Any] = field(default_factory=dict)
