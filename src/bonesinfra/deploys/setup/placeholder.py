from pyinfra.operations import files

from bonesinfra.infra.deploy_helpers import render


def seed(data, paths, here):
    render(
        "Seed placeholder index page",
        here / "assets/nginx/index.html.j2",
        paths["placeholder_index"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="0640",
        **data,
    )

    files.link(
        name="Point current symlink at placeholder release",
        path=paths["current"],
        target=paths["placeholder_release"],
        force=True,
        _sudo=True,
    )
