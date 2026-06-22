from pyinfra.operations import files

from bonesinfra.runtimes.common import php_fpm_pool


def setup_storage_directories(paths, ctx):
    runtime_user = ctx.runtime.runtime_user
    runtime_group = ctx.runtime.runtime_group
    subdirs = ["logs", "framework/cache", "framework/sessions", "framework/views"]
    for subdir in subdirs:
        files.directory(
            name=f"Ensure storage/{subdir} exists",
            path=f"{paths['shared']}/storage/{subdir}",
            user=runtime_user,
            group=runtime_group,
            mode="2771",
            _sudo=True,
        )


def setup_pool(here, ctx, paths, php_version):
    php_fpm_pool.ensure_log_dir(ctx)
    php_fpm_pool.render_pool(ctx, here=here, paths=paths, php_version=php_version)
    php_fpm_pool.validate_php_fpm(php_version)
    php_fpm_pool.reload_php_fpm(php_version)
