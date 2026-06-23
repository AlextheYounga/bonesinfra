from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service


def questions():
    return [
        {
            "key": "is_static",
            "type": "bool",
            "label": "Is this Nuxt site static?",
            "default": True,
        },
    ]


def deploy(ctx):
    is_static = ctx.runtime.runtime_data.get("is_static", True)
    paths = service.runtime_paths(ctx)

    if is_static:
        common_paths.ensure_runtime_dirs(ctx)
        nginx.render_static(ctx, paths=paths, root=".output/public")
        return

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
    service.render_app_service(
        ctx,
        paths=paths,
        name="nuxt",
        runtime_label="Nuxt app server",
        runtime_exec=(
            f"/usr/bin/env NODE_ENV=production NITRO_UNIX_SOCKET={socket_path} node .output/server/index.mjs"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "nuxt", apparmor_profile_name=apparmor_profile_name)
