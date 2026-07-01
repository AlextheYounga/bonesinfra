from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any

from bonesinfra.domain.paths import DeploymentPaths

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
        with Path(config_path).open("rb") as f:
            bones_cfg = tomllib.load(f)
        project_name = bones_cfg.get("project_name", "")
        repo_path = bones_cfg.get("repo_path", "")
        project_root = bones_cfg.get("project_root", "")
        host = bones_cfg.get("host", "")
        port = int(bones_cfg.get("port", DEFAULT_SSH_PORT))

        runtime_cfg = {}
        if runtime_config_path:
            rpath = Path(runtime_config_path)
            if rpath.exists():
                with rpath.open("rb") as f:
                    runtime_cfg = tomllib.load(f)

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
            shared_paths=_parse_shared_paths(runtime_cfg),
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
    def paths(self) -> DeploymentPaths:
        try:
            return self._paths
        except AttributeError:
            pass
        self._paths = DeploymentPaths.new(
            self.config.project_name,
            self.config.repo_path,
            self.config.project_root,
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
        "project_name": ctx.config.project_name,
        "project_root": ctx.config.project_root,
        "web_root": ctx.runtime.web_root,
        "repo_path": ctx.config.repo_path,
        "branch": ctx.config.branch,
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
    shared_paths: list[SharedPath] = field(default_factory=list)
    runtime_data: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SharedPath:
    path: str
    type: str


def _parse_shared_paths(runtime_cfg: dict[str, Any]) -> list[SharedPath]:
    shared = runtime_cfg.get("shared")
    if shared is None:
        return []
    if not isinstance(shared, dict):
        raise TypeError("runtime.toml [shared] must be a table")

    paths = shared.get("paths", [])
    if not isinstance(paths, list):
        raise TypeError("runtime.toml [shared].paths must be a list")

    return [_parse_shared_path(entry) for entry in paths]


def _parse_shared_path(entry: Any) -> SharedPath:
    if not isinstance(entry, dict):
        raise TypeError("runtime.toml [shared].paths entries must be tables")

    raw_path = entry.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        raise ValueError("runtime.toml [shared].paths entries need a non-empty string path")

    path = _validate_shared_path(raw_path)
    path_type = entry.get("type")
    if path_type not in {"file", "dir"}:
        raise ValueError(f"invalid shared path type for {path}: {path_type!r}")

    return SharedPath(path=path, type=path_type)


def _validate_shared_path(raw_path: str) -> str:
    if "\\" in raw_path:
        raise ValueError(f"invalid shared path {raw_path!r}: use forward slashes")
    if raw_path.startswith("/"):
        raise ValueError(f"invalid shared path {raw_path!r}: path must be relative")

    for part in raw_path.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError(f"invalid shared path {raw_path!r}: path must use normal components only")

    path = PurePosixPath(raw_path)

    parts = path.parts
    if not parts:
        raise ValueError("invalid shared path '': path must not be empty")

    for part in parts:
        if part in {"", ".", ".."}:
            raise ValueError(f"invalid shared path {raw_path!r}: path must use normal components only")

    return path.as_posix()
