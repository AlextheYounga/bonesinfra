from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service, validation


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    port = ctx.runtime.runtime_data.get("internal_port", 3100)
    node.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="next",
        apparmor_exec_paths=["/usr/bin/node"],
        apparmor_writable_paths=[],
        apparmor_network="network inet stream,",
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Next.js standalone server exists as runtime user",
        "test -f .next/standalone/server.js",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="next",
        runtime_label="Next.js app server",
        runtime_exec=(
            f"/usr/bin/env NODE_ENV=production PORT={port} HOSTNAME=127.0.0.1 "
            "node .next/standalone/server.js"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
        runtime_address_families="AF_UNIX AF_INET",
    )
    nginx.render_proxy(ctx, paths=paths, port=port)
    service.enable_and_start(ctx, "next")
