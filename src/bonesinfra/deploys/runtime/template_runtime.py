def load(ctx):
    template = ctx.runtime.runtime_data.get("template")
    if not template:
        return

    from bonesinfra.runtimes import get_runtime

    runtime = get_runtime(template)
    if not hasattr(runtime, "deploy"):
        raise RuntimeError(f"Runtime {template} does not expose deploy(ctx)")

    runtime.deploy(ctx)
