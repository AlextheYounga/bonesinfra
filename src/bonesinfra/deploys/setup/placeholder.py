
from pyinfra.operations import files


def seed(data, paths, here):
    files.template(
        name="Seed placeholder index page",
        src=str(here / "assets/nginx/index.html.j2"),
        dest=paths["placeholder_index"],
        user=data["deploy_user"],
        group=data["release_group"],
        mode="0640",
        **data,
        _sudo=True,
    )

    files.link(
        name="Point current symlink at placeholder release",
        path=paths["current"],
        target=paths["placeholder_release"],
        force=True,
        _sudo=True,
    )
