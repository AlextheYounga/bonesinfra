from __future__ import annotations

import sys
from collections.abc import Callable

from pyinfra.api import Config, Inventory, State
from pyinfra.api.connect import connect_all
from pyinfra.api.exceptions import PyinfraError
from pyinfra.api.operations import run_ops
from pyinfra.context import ctx_config, ctx_host, ctx_inventory, ctx_state

from bonesinfra.domain.context import DeployContext
from bonesinfra.infra.output import (
    BonesDeployCallback,
    activity,
    print_banner,
    print_connected,
    print_done,
    print_target,
    setup_output,
    stop_live_output,
)


def run(
    *,
    ctx: DeployContext,
    ssh_key: str | None = None,
    deploy: Callable[[DeployContext], None],
) -> None:
    setup_output()

    hostname = ctx.config.host
    ssh_user = ctx.config.ssh_user
    ssh_port = int(ctx.config.port)

    config = Config(SSH_USER=ssh_user, SSH_PORT=ssh_port)
    if ssh_key:
        config.SSH_KEY = ssh_key
        config.SSH_STRICT_HOST_KEY_CHECKING = False

    inventory = Inventory(([(hostname, {})], {}))
    state = State(inventory, config)
    target_host = next(iter(inventory))

    print_banner()
    print_target(hostname, ssh_user)

    try:
        with activity("connecting"):
            connect_all(state)
    except PyinfraError:
        print_done(success=False)
        sys.exit(1)

    print_connected()

    with (
        ctx_state.use(state),
        ctx_config.use(config),
        ctx_inventory.use(inventory),
        ctx_host.use(target_host),
        activity("planning deploy operations"),
    ):
        deploy(ctx)

    state.add_callback_handler(BonesDeployCallback())

    try:
        run_ops(state)
    except PyinfraError:
        stop_live_output()
        print_done(success=False)
        sys.exit(1)

    if state.failed_hosts:
        stop_live_output()
        print_done(success=False)
        sys.exit(1)

    stop_live_output()
    print_done(success=True)
