import tomllib
from pathlib import Path


def load_toml(path):
    with Path(path).open("rb") as file:
        return tomllib.load(file)


def load_runtime_config(deploy_file):
    return load_toml(str(Path(deploy_file).parent / "runtime.toml"))
