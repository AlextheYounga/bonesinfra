from __future__ import annotations

import sys
from collections.abc import Callable
from typing import Any

from pyinfra.api import Config, Inventory, State
from pyinfra.api.connect import connect_all
from pyinfra.api.exceptions import PyinfraError
from pyinfra.api.operations import run_ops
from pyinfra.context import ctx_config, ctx_host, ctx_inventory, ctx_state

from bonesinfra.infra.output import activity, print_banner, print_done, print_target, setup_output


def run(
    *,
    hostname: str,
    ssh_user: str,
    ssh_port: int = 22,
    ssh_key: str | None = None,
    data: dict[str, Any],
    deploy: Callable[[], None],
) -> None:
    setup_output()

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

    print_banner()
    print_target(hostname, ssh_user)

    try:
        connect_all(state)
    except PyinfraError:
        print_done(success=False)
        sys.exit(1)

    with ctx_state.use(state), ctx_config.use(config), ctx_inventory.use(inventory), ctx_host.use(target_host):
        with activity("planning deploy operations"):
            deploy()

    try:
        run_ops(state)
    except PyinfraError:
        print_done(success=False)
        sys.exit(1)

    if state.failed_hosts:
        print_done(success=False)
        sys.exit(1)

    print_done(success=True)
