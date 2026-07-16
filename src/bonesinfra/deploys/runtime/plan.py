from bonesinfra.deploys.runtime import apparmor, nginx, packages, template_runtime


def deploy_runtime(ctx):
    paths = ctx.paths_dict
    packages.install_apt(ctx)
    apparmor.setup(ctx, paths)
    nginx.setup(ctx, paths)
    template_runtime.load(ctx)
    nginx.start_services(paths)
