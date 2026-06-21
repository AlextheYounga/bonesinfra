from pathlib import PurePosixPath

from pyinfra.operations import files

from bonesinfra.infra.deploy_helpers import mkdir


def _shared_path_target(shared_root, raw_path):
    if not isinstance(raw_path, str) or not raw_path:
        raise ValueError("shared path is required")

    raw_parts = raw_path.split("/")
    rel_path = PurePosixPath(raw_path)
    if rel_path.is_absolute():
        raise ValueError(f"shared path must be relative: {raw_path}")
    if any(part in {"", ".", ".."} for part in raw_parts):
        raise ValueError(f"shared path contains unsafe components: {raw_path}")

    return str(PurePosixPath(shared_root, rel_path))


def provision(ctx, paths):
    runtime_user = ctx.runtime.runtime_user
    runtime_group = ctx.runtime.runtime_group
    shared_paths = ctx.runtime.runtime_data.get("shared", {}).get("paths", [])

    for item in shared_paths:
        if not isinstance(item, dict):
            raise TypeError(f"shared path entry must be a table: {item!r}")

        raw_path = item.get("path")
        path_type = item.get("type")
        target = _shared_path_target(paths["shared"], raw_path)

        if path_type == "dir":
            mkdir(
                name=f"Ensure shared directory exists: {raw_path}",
                path=target,
                user=runtime_user,
                group=runtime_group,
                mode="0775",
            )
            continue

        if path_type != "file":
            raise ValueError(f"unsupported shared path type for {raw_path}: {path_type}")

        parent = str(PurePosixPath(target).parent)
        mkdir(
            name=f"Ensure parent directory exists for shared file: {raw_path}",
            path=parent,
            user=runtime_user,
            group=runtime_group,
            mode="0775",
        )
        files.file(
            name=f"Ensure shared file exists: {raw_path}",
            path=target,
            user=runtime_user,
            group=runtime_group,
            mode="0640",
            touch=True,
            _sudo=True,
        )
