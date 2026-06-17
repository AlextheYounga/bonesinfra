import tomllib
from pathlib import Path


def load_toml(path):
    with Path(path).open("rb") as file:
        return tomllib.load(file)


def load_runtime_config(deploy_file):
    return load_toml(str(Path(deploy_file).parent / "runtime.toml"))


def unflatten(data_dict):
    result = {}
    for key, value in data_dict.items():
        parts = key.split(".")
        node = result
        for part in parts[:-1]:
            if part not in node:
                node[part] = {}
            node = node[part]
        node[parts[-1]] = value
    return result
