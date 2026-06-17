import tomllib
from pathlib import Path
from typing import Any


def load_toml(path: str) -> dict[str, Any]:
    with Path(path).open("rb") as file:
        return tomllib.load(file)


def load_runtime_config(deploy_file: str) -> dict[str, Any]:
    return load_toml(str(Path(deploy_file).parent / "runtime.toml"))
