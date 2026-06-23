from pyinfra.operations import server

from bonesinfra.runtimes.common import php_fpm_pool


def cleanup_orphaned_pools(ctx, php_version):
    project = ctx.config.project_name
    current_pool = php_fpm_pool.pool_config_path(project, php_version)
    command = "\n".join(
        [
            f'project="{project}"',
            f'current_pool="{current_pool}"',
            'for pool in /etc/php/*/fpm/pool.d/"$project".conf; do',
            '  [ -e "$pool" ] || continue',
            '  [ "$pool" = "$current_pool" ] && continue',
            "  version=${pool#/etc/php/}",
            "  version=${version%%/*}",
            '  rm -f "$pool"',
            '  systemctl reload-or-restart "php${version}-fpm"',
            "done",
        ]
    )
    server.shell(
        name="Remove orphaned Laravel PHP-FPM pools from other PHP versions",
        commands=[command],
        _sudo=True,
    )


def setup_pool(here, ctx, paths, php_version):
    php_fpm_pool.ensure_log_dir(ctx)
    cleanup_orphaned_pools(ctx, php_version)
    php_fpm_pool.render_pool(ctx, here=here, paths=paths, php_version=php_version)
    php_fpm_pool.validate_php_fpm(php_version)
    php_fpm_pool.reload_php_fpm(php_version)
