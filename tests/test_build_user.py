from bonesinfra.deploys.setup.users import (
    build_group_for,
    build_home_for,
    build_user_for,
)


def test_build_identity_is_derived_from_project_name():
    assert build_user_for("demo") == "demo-build"
    assert build_group_for("demo") == "demo-build"
    assert build_home_for("demo") == "/var/lib/bonesdeploy/users/demo-build"
