"""CLI commands must run without crashing."""

import subprocess

from . import helpers

PYTHON = helpers.PYTHON_BIN
PYTHON_ENV = helpers.PYTHON_ENV


def _run_no_input(*args):
    return subprocess.run(
        [PYTHON, "-m", "bonesinfra", *args],
        capture_output=True,
        text=True,
        timeout=10,
        env=PYTHON_ENV,
        check=False,
    )


def test_runtime_list():
    result = _run_no_input("runtime", "list")
    assert result.returncode == 0, result.stderr


def test_runtime_questions_all():
    for name in ["django", "laravel", "next", "rails", "sveltekit", "vue"]:
        result = _run_no_input("runtime", "questions", name)
        assert result.returncode == 0, f"{name}: {result.stderr}"


def test_setup_apply_rejects_missing_host():
    result = _run_no_input("setup", "apply", "--config", "/dev/null")
    assert result.returncode == 3, f"Expected exit 3 for missing host, got {result.returncode}"
    assert "missing host" in result.stderr.lower()


def test_runtime_apply_requires_ssh_user():
    result = _run_no_input("runtime", "apply", "--config", "/dev/null", "--runtime-config", "/dev/null")
    assert result.returncode != 0, "Expected non-zero exit for missing --ssh-user"


def test_ssl_apply_rejects_missing_host():
    result = _run_no_input("ssl", "apply", "--config", "/dev/null")
    assert result.returncode == 3, f"Expected exit 3 for missing host, got {result.returncode}"
    assert "missing host" in result.stderr.lower()
