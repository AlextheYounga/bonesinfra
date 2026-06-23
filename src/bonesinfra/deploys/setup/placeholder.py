from pathlib import Path

from pyinfra.operations import files

from bonesinfra.domain.context import template_data
from bonesinfra.infra.deploy_helpers import mkdir, render


def seed(ctx, paths, here):
    render(
        "Seed placeholder index page",
        here / "assets/nginx/index.html.j2",
        paths["placeholder_index"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="0640",
        **template_data(ctx, paths=paths),
    )

    if ctx.runtime.runtime_data.get("template") == "nuxt" and ctx.runtime.runtime_data.get("is_static", True):
        nuxt_static_web_root = str(Path(paths["placeholder_release"]) / ".output/public")
        mkdir(
            name="Ensure Nuxt static placeholder output directory exists",
            path=nuxt_static_web_root,
            user=ctx.config.deploy_user,
            group=ctx.runtime.release_group,
            mode="0750",
        )
        render(
            "Seed Nuxt static placeholder index page",
            here / "assets/nginx/index.html.j2",
            str(Path(nuxt_static_web_root) / "index.html"),
            user=ctx.config.deploy_user,
            group=ctx.runtime.release_group,
            mode="0640",
            **template_data(ctx, paths=paths),
        )

    files.link(
        name="Point current symlink at placeholder release",
        path=paths["current"],
        target=paths["placeholder_release"],
        force=True,
        _sudo=True,
    )
