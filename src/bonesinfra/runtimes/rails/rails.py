from bonesinfra.runtimes.common import apparmor, logs, nginx, paths as common_paths, ruby, service, validation


def questions():
    return [
        {
            "key": "ruby_version",
            "type": "choice",
            "label": "Ruby version",
            "choices": ["3.2", "3.3", "3.4"],
            "default": "3.3",
        },
        {
            "key": "install_postgres",
            "type": "bool",
            "label": "Install PostgreSQL client libraries?",
            "default": False,
        },
        {
            "key": "install_redis",
            "type": "bool",
            "label": "Install Redis?",
            "default": False,
        },
        {
            "key": "rails_env",
            "type": "text",
            "label": "Rails environment",
            "default": "production",
        },
    ]


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/puma/puma.sock"
    runtime_write_paths = [
        f"{paths['current']}/tmp",  # noqa: S108
        f"{paths['current']}/log",
        f"{paths['current']}/storage",
    ]
    rails_env = ctx.runtime.runtime_data.get("rails_env", "production")
    ruby.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="puma",
        apparmor_exec_paths=["/usr/bin/ruby*", "/usr/bin/bundle*"],
        apparmor_writable_paths=runtime_write_paths,
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Puma availability as runtime user",
        "bundle exec puma --help >/dev/null",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="puma",
        runtime_label="Puma",
        runtime_exec=f"/usr/bin/env RAILS_ENV={rails_env} bundle exec puma -e {rails_env} -b unix://{socket_path}",
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=runtime_write_paths,
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "puma", apparmor_profile_name=apparmor_profile_name)
