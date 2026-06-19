from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service, validation


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/nuxt/nuxt.sock"
    node.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="nuxt",
        apparmor_exec_paths=["/usr/bin/node"],
        apparmor_writable_paths=[],
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Nuxt server entrypoint exists as runtime user",
        "test -f .output/server/index.mjs",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="nuxt",
        runtime_label="Nuxt app server",
        runtime_exec=(
            f"/usr/bin/env NODE_ENV=production NITRO_UNIX_SOCKET={socket_path} "
            "node .output/server/index.mjs"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "nuxt", apparmor_profile_name=apparmor_profile_name)
