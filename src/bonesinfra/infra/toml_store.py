import tomllib
from pathlib import Path
from typing import Any


def load_toml(path: str) -> dict[str, Any]:
    with Path(path).open("rb") as file:
        return tomllib.load(file)
