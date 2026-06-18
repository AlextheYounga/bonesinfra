from shlex import quote

from pyinfra.operations import server


def run_as_runtime_user(ctx, name, command):
    """Validate a runtime command as the runtime user, never as root.

    Root provisioning must not also be the thing that proves the service can
    start: a root-owned validation artifact (e.g. a log file) would later be
    unwritable by the service. Runs the command with HOME/XDG_CONFIG_HOME set
    so user-scoped config resolution matches the real service environment.
    """
    user = ctx.runtime.runtime_user
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    wrapped = f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"
    server.shell(
        name=name,
        commands=[wrapped],
        _sudo=True,
        _sudo_user=user,
    )
