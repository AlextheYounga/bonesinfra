import pytest

from bonesinfra.deploys.setup.users import (
    build_group_for,
    build_home_for,
    build_user_for,
    cpu_quota_for,
)


def test_build_identity_is_derived_from_project_name():
    assert build_user_for("demo") == "demo-build"
    assert build_group_for("demo") == "demo-build"
    assert build_home_for("demo") == "/var/lib/bonesdeploy/users/demo-build"


@pytest.mark.parametrize(
    ("online_cpu_count", "quota"),
    [(1, "75%"), (2, "150%"), (4, "300%"), (8, "600%")],
)
def test_cpu_quota_is_three_quarters_of_online_cpu_capacity(online_cpu_count, quota):
    assert cpu_quota_for(online_cpu_count) == quota


def test_cpu_quota_rejects_missing_online_cpus():
    with pytest.raises(ValueError, match="positive"):
        cpu_quota_for(0)
