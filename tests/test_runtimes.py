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


def test_laravel_php_fpm_validates_as_runtime_user():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_contains(content, "validation.run_as_runtime_user")
    helpers.assert_contains(content, "Validate PHP-FPM configuration as runtime user")


def test_laravel_php_fpm_does_not_validate_as_root():
    """Regression guard: php-fpm --test must never run as root.

    Root-owned validation created root-owned log files the runtime user
    could not write. Validation must go through validation.run_as_runtime_user.
    """
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    assert content.count("--test --fpm-config") == 1
    helpers.assert_not_contains(content, "_user_env_command")


def test_common_validation_runs_as_runtime_user_not_root():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/validation.py")
    helpers.assert_contains(content, "_sudo_user=user")
    helpers.assert_contains(content, "def run_as_runtime_user(ctx, name, command):")


def test_common_logs_provisions_runtime_owned_dir():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/logs.py")
    helpers.assert_contains(content, "/var/log/bonesdeploy")
    helpers.assert_contains(content, "user=ctx.runtime.runtime_user")
    helpers.assert_contains(content, 'name="Ensure BonesDeploy log root exists"')


def test_template_runtime_load_fails_loudly_without_silent_swallow():
    content = helpers.read(
        helpers.SRC_DIR / "bonesinfra/deploys/runtime/template_runtime.py"
    )
    helpers.assert_not_contains(content, "except (ImportError, KeyError)")
    helpers.assert_not_contains(content, "    pass")
    helpers.assert_contains(content, 'raise RuntimeError(f"Runtime {template} does not expose deploy(ctx)")')


def test_template_runtime_load_requires_deploy_attribute():
    content = helpers.read(
        helpers.SRC_DIR / "bonesinfra/deploys/runtime/template_runtime.py"
    )
    helpers.assert_contains(content, 'if not hasattr(runtime, "deploy")')


def test_all_runtimes_use_common_service_layer():
    """Non-Laravel dynamic runtimes must wire through common.service, not pass."""
    runtime_to_module_file = {
        "django": "bonesinfra/runtimes/django/django.py",
        "next": "bonesinfra/runtimes/next/next.py",
        "nuxt": "bonesinfra/runtimes/nuxt/nuxt.py",
        "rails": "bonesinfra/runtimes/rails/rails.py",
        "sveltekit": "bonesinfra/runtimes/sveltekit/svelte.py",
        "vue": "bonesinfra/runtimes/vue/vue.py",
    }
    for name, rel in runtime_to_module_file.items():
        content = helpers.read(helpers.SRC_DIR / rel)
        helpers.assert_not_contains(content, "    pass", msg=name)
        helpers.assert_contains(content, "service.runtime_paths(ctx)", msg=name)


def test_vue_is_static_only():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/vue/vue.py")
    helpers.assert_contains(content, "nginx.render_static")
    helpers.assert_not_contains(content, "render_app_service")


def test_next_uses_tcp_localhost():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/next/next.py")
    helpers.assert_contains(content, "HOSTNAME=127.0.0.1")
    helpers.assert_contains(content, "port=port")
    helpers.assert_contains(content, 'runtime_address_families="AF_UNIX AF_INET"')


def test_nuxt_uses_nitro_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/nuxt/nuxt.py")
    helpers.assert_contains(content, "NITRO_UNIX_SOCKET=")
    helpers.assert_contains(content, "socket_path=socket_path")


def test_sveltekit_uses_socket_path_env():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/sveltekit/svelte.py")
    helpers.assert_contains(content, "SOCKET_PATH=")
    helpers.assert_contains(content, "ORIGIN=")


def test_django_uses_gunicorn_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/django/django.py")
    helpers.assert_contains(content, "gunicorn")
    helpers.assert_contains(content, "--bind unix:")
    helpers.assert_contains(content, "wsgi_module")
    helpers.assert_not_contains(content, "python3-gunicorn")


def test_rails_uses_puma_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/rails/rails.py")
    helpers.assert_contains(content, "bundle exec puma")
    helpers.assert_contains(content, "-b unix://")
