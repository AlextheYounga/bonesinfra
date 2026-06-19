from bonesinfra.runtimes.common import apparmor, logs, nginx, paths as common_paths, python, service, validation


def questions():
    return [
        {
            "key": "wsgi_module",
            "type": "text",
            "label": "WSGI module",
            "default": "config.wsgi:application",
        },
        {
            "key": "python_version",
            "type": "choice",
            "label": "Python version",
            "choices": ["3.11", "3.12", "3.13"],
            "default": "3.12",
        },
        {
            "key": "install_postgres",
            "type": "bool",
            "label": "Install PostgreSQL client libraries?",
            "default": False,
        },
        {
            "key": "static_root",
            "type": "text",
            "label": "Static root",
            "default": "staticfiles",
        },
        {
            "key": "media_root",
            "type": "text",
            "label": "Media root",
            "default": "media",
        },
    ]


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/gunicorn/gunicorn.sock"
    wsgi_module = ctx.runtime.runtime_data.get("wsgi_module", "config.wsgi:application")
    static_root = f"{paths['current']}/{ctx.runtime.runtime_data.get('static_root', 'staticfiles')}"
    media_root = f"{paths['current']}/{ctx.runtime.runtime_data.get('media_root', 'media')}"
    writable = [static_root, media_root]
    gunicorn_bin = f"{paths['current']}/.venv/bin/gunicorn"
    python.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="gunicorn",
        apparmor_exec_paths=[gunicorn_bin],
        apparmor_writable_paths=writable,
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Gunicorn configuration as runtime user",
        f"{gunicorn_bin} --check-config {wsgi_module}",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="gunicorn",
        runtime_label="Gunicorn",
        runtime_exec=f"{gunicorn_bin} {wsgi_module} --bind unix:{socket_path}",
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=writable,
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "gunicorn", apparmor_profile_name=apparmor_profile_name)
