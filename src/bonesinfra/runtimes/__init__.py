import importlib
import sys

_REGISTRY = {}

_MODULE_PATHS = {
    "laravel": "bonesinfra.runtimes.laravel",
    "django": "bonesinfra.runtimes.django.django",
    "next": "bonesinfra.runtimes.next.next",
    "rails": "bonesinfra.runtimes.rails.rails",
    "sveltekit": "bonesinfra.runtimes.sveltekit.svelte",
    "vue": "bonesinfra.runtimes.vue.vue",
}


def _discover():
    for name, module_path in _MODULE_PATHS.items():
        try:
            module = importlib.import_module(module_path)
            _REGISTRY[name] = module
        except ImportError:
            pass


_discover()


def list_runtimes():
    return sorted(_REGISTRY.keys())


def get_runtime(name):
    module = _REGISTRY.get(name)
    if module is None:
        print(f"Unknown runtime: {name}. Available: {', '.join(list_runtimes())}", file=sys.stderr)
        sys.exit(1)
    return module
