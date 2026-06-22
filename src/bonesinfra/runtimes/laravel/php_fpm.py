from bonesinfra.runtimes.common import php_fpm_pool


def setup_pool(here, ctx, paths, php_version):
    php_fpm_pool.ensure_log_dir(ctx)
    php_fpm_pool.render_pool(ctx, here=here, paths=paths, php_version=php_version)
    php_fpm_pool.validate_php_fpm(php_version)
    php_fpm_pool.reload_php_fpm(php_version)
