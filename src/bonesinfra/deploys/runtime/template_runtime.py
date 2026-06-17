def load(data):
    template = data.get("template")
    if not template:
        return
    try:
        from bonesinfra.runtimes import get_runtime

        mod = get_runtime(template)
        if hasattr(mod, "deploy"):
            mod.deploy()
    except (ImportError, KeyError):
        pass
