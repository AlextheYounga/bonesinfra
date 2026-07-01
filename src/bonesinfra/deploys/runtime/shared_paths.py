from shlex import quote

from pyinfra.operations import server


def ensure(ctx, paths):
    for shared_path in ctx.runtime.shared_paths:
        if shared_path.type == "dir":
            _ensure_dir(paths["shared"], shared_path.path, ctx.runtime.runtime_user, ctx.runtime.runtime_group)
            continue

        _ensure_file(paths["shared"], shared_path.path, ctx.runtime.runtime_user, ctx.runtime.runtime_group)


def _ensure_dir(shared_root: str, relative_path: str, runtime_user: str, runtime_group: str):
    target = f"{shared_root}/{relative_path}"
    server.shell(
        name=f"Ensure shared directory {relative_path}",
        commands=[(f"install -d -o {quote(runtime_user)} -g {quote(runtime_group)} -m 0750 {quote(target)}")],
        _sudo=True,
    )


def _ensure_file(shared_root: str, relative_path: str, runtime_user: str, runtime_group: str):
    target = f"{shared_root}/{relative_path}"
    parent = target.rsplit("/", 1)[0]
    user = "root" if _is_dotenv(relative_path) else runtime_user
    server.shell(
        name=f"Ensure shared file {relative_path}",
        commands=[
            (
                f"install -d -o {quote(runtime_user)} -g {quote(runtime_group)} -m 0750"
                f" {quote(parent)}"
                f" && touch {quote(target)}"
                f" && chown {quote(user)}:{quote(runtime_group)} {quote(target)}"
                f" && chmod 0640 {quote(target)}"
            )
        ],
        _sudo=True,
    )


def _is_dotenv(relative_path: str) -> bool:
    return relative_path.rsplit("/", 1)[-1] == ".env"
