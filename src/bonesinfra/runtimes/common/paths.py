from pyinfra.operations import files

from bonesinfra.domain.paths import RUNTIME_SOCKET_PARENT


def ensure_runtime_dirs(ctx):
    """Create /run/<project> as the runtime user before validation or service start.

    RuntimeDirectory= in the systemd unit also does this at start time, but
    validation runs before start, so we provision it here too.
    """
    project = ctx.config.project_name
    files.directory(
        name="Ensure runtime socket directory exists",
        path=f"{RUNTIME_SOCKET_PARENT}/{project}",
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0750",
        _sudo=True,
    )
