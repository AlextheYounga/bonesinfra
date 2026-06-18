from shlex import quote

from pyinfra.operations import server


def _user_env_command(user, command):
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    return f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"


def run(data):
    server.shell(
        name="Run bonesremote doctor as deploy user",
        commands=[_user_env_command(data["deploy_user"], "/usr/local/bin/bonesremote doctor")],
        _sudo=True,
        _sudo_user=data["deploy_user"],
    )
