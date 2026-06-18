from __future__ import annotations

import logging

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console(stderr=True)
_err = Console(stderr=True)


def setup_output() -> None:
    from pyinfra.api.output import set_echo, set_formatter

    def bones_echo(message=None, **kwargs):
        if message is not None:
            _err.print(message, highlight=False)

    def bones_format(text, *args, **kwargs):
        return text

    set_echo(bones_echo)
    set_formatter(bones_format)

    pyinfra_logger = logging.getLogger("pyinfra")
    pyinfra_logger.handlers.clear()
    pyinfra_logger.addHandler(RichHandler(console=console, show_time=False, show_path=False))
    pyinfra_logger.setLevel(logging.INFO)
    pyinfra_logger.propagate = False


def print_banner() -> None:
    console.print()
    title = Text("☠  bonesdeploy", style="bold cyan")
    console.print(Panel(title, border_style="cyan"))


def print_target(hostname: str, user: str) -> None:
    info = Table.grid(padding=(0, 1))
    info.add_column(style="dim")
    info.add_column(style="bold yellow")
    info.add_row("target:", f"{user}@{hostname}")
    console.print(info)
    console.print()


def print_done(success: bool) -> None:
    console.print()
    if success:
        console.print("☠  [bold green]deploy complete[/]")
    else:
        console.print("☠  [bold red]deploy failed[/]")
    console.print()
