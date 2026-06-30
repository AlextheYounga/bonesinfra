"""Tests for shared-path provisioning removal.

BonesInfra no longer creates framework shared paths.
It creates only project_root/shared with mode 0750.
"""

from . import helpers

SETUP_DIRECTORIES = helpers.SRC_DIR / "bonesinfra/deploys/setup/directories.py"
SETUP_USERS = helpers.SRC_DIR / "bonesinfra/deploys/setup/users.py"
RUNTIME_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/runtime/plan.py"
LARAVEL_PHP_FPM = helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py"
LARAVEL_DEPLOY = helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py"
SHARED_PATHS_PY = helpers.SRC_DIR / "bonesinfra/deploys/runtime/shared_paths.py"
RAILS_DEPLOY = helpers.SRC_DIR / "bonesinfra/runtimes/rails/rails.py"
DJANGO_DEPLOY = helpers.SRC_DIR / "bonesinfra/runtimes/django/django.py"


def test_shared_paths_module_is_deleted():
    assert not SHARED_PATHS_PY.exists(), "shared_paths.py must be deleted"


def test_shared_root_is_created_with_mode_0750():
    c = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c, 'path=paths["shared"]')
    helpers.assert_contains(c, 'mode="0750"')


def test_deploy_user_is_not_added_to_runtime_group():
    c = helpers.read(SETUP_USERS)
    helpers.assert_not_contains(c, "_ensure_group_membership(ctx.config.deploy_user, ctx.runtime.runtime_group)")


def test_laravel_does_not_create_storage_subdirectories():
    c = helpers.read(LARAVEL_PHP_FPM)
    helpers.assert_not_contains(c, "setup_storage_directories")
    helpers.assert_not_contains(c, "storage/logs")
    helpers.assert_not_contains(c, "framework/cache")
    helpers.assert_not_contains(c, "framework/sessions")
    helpers.assert_not_contains(c, "framework/views")


def test_runtime_write_paths_are_shared_paths():
    rails = helpers.read(RAILS_DEPLOY)
    helpers.assert_contains(rails, "f\"{paths['shared']}/tmp\"")
    helpers.assert_contains(rails, "f\"{paths['shared']}/log\"")
    helpers.assert_contains(rails, "f\"{paths['shared']}/storage\"")

    django = helpers.read(DJANGO_DEPLOY)
    helpers.assert_contains(django, "f\"{paths['shared']}/staticfiles\"")
    helpers.assert_contains(django, "f\"{paths['shared']}/media\"")
