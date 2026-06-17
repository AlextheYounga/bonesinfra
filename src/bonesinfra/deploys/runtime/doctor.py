from pyinfra.operations import server


def run(data):
    server.shell(
        name="Run bonesremote doctor as deploy user",
        commands=["/usr/local/bin/bonesremote doctor"],
        _sudo=True,
        _sudo_user=data["deploy_user"],
    )
