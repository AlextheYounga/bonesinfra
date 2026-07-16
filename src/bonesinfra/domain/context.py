from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from bonesinfra.domain.paths import DEFAULT_PROJECT_ROOT_PARENT, DEFAULT_REPO_PARENT, DeploymentPaths

DEPLOY_USER = "git"

DEFAULT_SSH_USER = "root"
DEFAULT_SSH_PORT = "22"
DEFAULT_WEB_ROOT = "public"
DEFAULT_BUILD_CPU_QUOTA_PERCENT = 75
DEFAULT_BUILD_MEMORY_HIGH_PERCENT = 60
DEFAULT_BUILD_MEMORY_MAX_PERCENT = 75


@dataclass
class DeployContext:
    app: AppConfig
    build: BuildConfig
    runtime: RuntimeConfig

    @classmethod
    def from_files(cls, config_path: str) -> DeployContext:
        with Path(config_path).open("rb") as f:
            bones_cfg = tomllib.load(f)
        app_cfg = _table(bones_cfg, "app")
        server_cfg = _table(app_cfg, "server")
        dns_cfg = _table(app_cfg, "dns")
        deploy_cfg = _table(app_cfg, "deploy")
        build_cfg = _table(bones_cfg, "build")
        resources_cfg = _table(build_cfg, "resources")
        runtime_cfg = _table(bones_cfg, "runtime")
        project_name = str(app_cfg.get("project_name", ""))

        app = AppConfig(
            project_name=project_name,
            repo_path=str(app_cfg.get("repo_path") or f"{DEFAULT_REPO_PARENT}/{project_name}.git"),
            project_root=str(app_cfg.get("project_root") or f"{DEFAULT_PROJECT_ROOT_PARENT}/{project_name}"),
            server=ServerConfig(
                host=str(server_cfg.get("host", "")),
                ssh_user=str(server_cfg.get("ssh_user", DEFAULT_SSH_USER)),
                port=str(int(server_cfg.get("port", DEFAULT_SSH_PORT))),
            ),
            dns=DnsConfig(
                domain=str(dns_cfg.get("domain", "")),
                preview_domain=str(dns_cfg.get("preview_domain", "")),
                email=str(dns_cfg.get("email", "")),
                ssl_enabled=bool(dns_cfg.get("ssl_enabled", False)),
            ),
            deploy=DeployConfig(branch=str(deploy_cfg.get("branch", "master"))),
        )
        build = BuildConfig(
            resources=BuildResourceLimits(
                cpu_quota_percent=int(resources_cfg.get("cpu_quota_percent", DEFAULT_BUILD_CPU_QUOTA_PERCENT)),
                memory_high_percent=int(resources_cfg.get("memory_high_percent", DEFAULT_BUILD_MEMORY_HIGH_PERCENT)),
                memory_max_percent=int(resources_cfg.get("memory_max_percent", DEFAULT_BUILD_MEMORY_MAX_PERCENT)),
            ),
        )

        runtime = RuntimeConfig(
            web_root=str(runtime_cfg.get("web_root") or DEFAULT_WEB_ROOT),
            runtime_user=str(runtime_cfg.get("runtime_user") or project_name),
            runtime_group=str(runtime_cfg.get("runtime_group") or project_name),
            data={
                key: value
                for key, value in runtime_cfg.items()
                if key not in {"web_root", "runtime_user", "runtime_group", "permissions", "release_group", "shared"}
            },
        )

        return cls(app=app, build=build, runtime=runtime)

    @property
    def paths(self) -> DeploymentPaths:
        try:
            return self._paths
        except AttributeError:
            pass
        self._paths = DeploymentPaths.new(
            self.app.project_name,
            self.app.repo_path,
            self.app.project_root,
            self.runtime.web_root,
        )
        return self._paths

    @property
    def paths_dict(self) -> dict[str, Any]:
        return self.paths.__dict__


def template_data(ctx: DeployContext, *, paths: dict[str, Any] | None = None, **extra: Any) -> dict[str, Any]:
    """Build flat template context from DeployContext for Jinja2 template rendering."""
    if paths is None:
        paths = ctx.paths_dict

    data: dict[str, Any] = {
        "project_name": ctx.app.project_name,
        "project_root": paths["project_root"],
        "web_root": ctx.runtime.web_root,
        "repo_path": paths["repo"],
        "branch": ctx.app.deploy.branch,
        "deploy_user": DEPLOY_USER,
        "runtime_user": ctx.runtime.runtime_user,
        "runtime_group": ctx.runtime.runtime_group,
        "project_root_parent": paths["project_root_parent"],
        "ssh_port": int(ctx.app.server.port),
        "paths": paths,
        "ssl_domain": ctx.app.dns.domain,
        "ssl_email": ctx.app.dns.email,
        "preview_domain": ctx.app.dns.preview_domain,
    }

    for key, value in ctx.runtime.data.items():
        if key not in data:
            data[key] = value

    data.update(extra)
    return data


@dataclass(frozen=True)
class BuildResourceLimits:
    cpu_quota_percent: int = DEFAULT_BUILD_CPU_QUOTA_PERCENT
    memory_high_percent: int = DEFAULT_BUILD_MEMORY_HIGH_PERCENT
    memory_max_percent: int = DEFAULT_BUILD_MEMORY_MAX_PERCENT

    def __post_init__(self) -> None:
        for name, value in (
            ("cpu_quota_percent", self.cpu_quota_percent),
            ("memory_high_percent", self.memory_high_percent),
            ("memory_max_percent", self.memory_max_percent),
        ):
            if type(value) is not int or not 1 <= value <= 100:  # noqa: PLR2004
                raise ValueError(f"{name} must be an integer from 1 to 100")
        if self.memory_high_percent > self.memory_max_percent:
            raise ValueError("memory_high_percent must not exceed memory_max_percent")


@dataclass
class AppConfig:
    project_name: str
    repo_path: str
    project_root: str
    server: ServerConfig
    dns: DnsConfig
    deploy: DeployConfig


@dataclass
class ServerConfig:
    ssh_user: str
    host: str
    port: str


@dataclass
class DnsConfig:
    domain: str
    preview_domain: str
    email: str
    ssl_enabled: bool


@dataclass
class DeployConfig:
    branch: str


@dataclass
class BuildConfig:
    resources: BuildResourceLimits = field(default_factory=BuildResourceLimits)


@dataclass
class RuntimeConfig:
    web_root: str
    runtime_user: str
    runtime_group: str
    data: dict[str, Any] = field(default_factory=dict)


def _table(parent: dict[str, Any], name: str) -> dict[str, Any]:
    value = parent.get(name, {})
    if not isinstance(value, dict):
        raise TypeError(f"bones.toml [{name}] must be a table")
    return value
