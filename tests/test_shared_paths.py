import pytest

from bonesinfra.deploys.runtime import shared_paths

from . import helpers


@pytest.mark.parametrize(
    "raw_path",
    ["/etc/passwd", "../storage", "storage/../logs", "./storage", "storage/./logs", "storage//logs"],
)
def test_shared_path_target_rejects_unsafe_paths(raw_path):
    with pytest.raises(ValueError):
        shared_paths._shared_path_target("/srv/sites/myapp/shared", raw_path)


def test_runtime_plan_provisions_shared_paths_before_runtime_template():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/plan.py")
    helpers.assert_ordering(
        content,
        "nginx.setup",
        "shared_paths.provision",
        "template_runtime.load",
    )


def test_laravel_storage_directories_use_shared_root():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_contains(content, "paths['shared']")
    helpers.assert_not_contains(content, "paths['current']}/storage")
