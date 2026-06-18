from bonesinfra.runtimes.common import nginx, service


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    nginx.render_static(ctx, paths=paths)
