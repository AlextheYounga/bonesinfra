"""Every runtime module must export questions() and deploy()."""

import importlib

from . import helpers

RUNTIMES_MODULES = {
    "laravel": "bonesinfra.runtimes.laravel",
    "django": "bonesinfra.runtimes.django.django",
    "next": "bonesinfra.runtimes.next.next",
    "nuxt": "bonesinfra.runtimes.nuxt.nuxt",
    "rails": "bonesinfra.runtimes.rails.rails",
    "sveltekit": "bonesinfra.runtimes.sveltekit.svelte",
    "vue": "bonesinfra.runtimes.vue.vue",
}


def test_runtimes_have_questions_and_deploy():
    for name, module_path in RUNTIMES_MODULES.items():
        mod = importlib.import_module(module_path)
        assert callable(getattr(mod, "questions", None)), f"{name}: missing questions()"
        assert callable(getattr(mod, "deploy", None)), f"{name}: missing deploy()"


def test_laravel_uses_host_data():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py")
    helpers.assert_contains(content, "host.data", "laravel must use host.data")
