from __future__ import annotations

import sys
from collections.abc import Callable
from typing import Any

from pyinfra.api import Config, Inventory, State
from pyinfra.api.connect import connect_all
from pyinfra.api.operations import run_ops
from pyinfra.context import ctx_config, ctx_host, ctx_inventory, ctx_state


def run(
    *,
    hostname: str,
    ssh_user: str,
    ssh_port: int = 22,
    ssh_key: str | None = None,
    data: dict[str, Any],
    deploy: Callable[[], None],
) -> None:
    data = dict(data)
    data["ssh_user"] = ssh_user
    data["ssh_port"] = int(data.get("ssh_port", ssh_port))
    if ssh_key:
        data["ssh_key"] = ssh_key

    config = Config(SSH_USER=ssh_user, SSH_PORT=ssh_port)
    if ssh_key:
        config.SSH_KEY = ssh_key
        config.SSH_STRICT_HOST_KEY_CHECKING = False

    inventory = Inventory(([(hostname, data)], {}))
    state = State(inventory, config)
    target_host = next(iter(inventory))

    connect_all(state)

    with ctx_state.use(state), ctx_config.use(config), ctx_inventory.use(inventory), ctx_host.use(target_host):
        deploy()

    run_ops(state)

    if state.failed_hosts:
        print("pyinfra deploy completed with failures.", file=sys.stderr)
        sys.exit(1)
