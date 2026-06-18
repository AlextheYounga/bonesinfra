import importlib

from bonesinfra.app import runtime_catalog
from bonesinfra.runtimes import list_runtimes

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


def test_runtime_registry_is_explicit():
    assert list_runtimes() == sorted(RUNTIMES_MODULES)


def test_laravel_questions_are_exposed():
    assert runtime_catalog.get_questions("laravel")


def test_laravel_deploy_accepts_ctx():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py")
    helpers.assert_contains(content, "def deploy(ctx):", "laravel deploy must accept ctx")
