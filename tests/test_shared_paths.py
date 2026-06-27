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


def test_shared_paths_module_is_deleted():
    assert not SHARED_PATHS_PY.exists(), "shared_paths.py must be deleted"


def test_runtime_plan_does_not_call_shared_paths():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_not_contains(c, "shared_paths")
    helpers.assert_not_contains(c, "shared.paths")


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


def test_laravel_deploy_does_not_call_storage_setup():
    c = helpers.read(LARAVEL_DEPLOY)
    helpers.assert_not_contains(c, "setup_storage_directories")


def test_bonesinfra_does_not_create_env_file():
    # BonesInfra must not create shared/.env anywhere
    for f in [SETUP_DIRECTORIES, RUNTIME_PLAN, LARAVEL_PHP_FPM, LARAVEL_DEPLOY]:
        c = helpers.read(f)
        helpers.assert_not_contains(c, "touch")
        # Only "exists" is from non-file-creation contexts like "project not exists"
        if ".env" in c:
            assert "Ensure shared file" not in c, f"{f} must not create .env"


def test_runtime_plan_does_not_inspect_shared_in_runtime_data():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_not_contains(c, '["shared"]')
