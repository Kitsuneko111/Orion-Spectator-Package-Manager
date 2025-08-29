import typing as t
from typing import Optional, Any

from click import Context
from typing_extensions import Annotated

import typer

from typer.core import TyperGroup

from utils.generate_version import version

from commands import commands
from callbacks import callbacks

app = typer.Typer()


# Pre-injection wrapper for any callback
# Yes I gave up and used AI here, sue me it's a hard injection to do
def with_context(callback):
    def wrapper(value, ctx: typer.Context):
        if ctx.obj is None:
            ctx.obj = {}
        ctx.obj["version"] = "1.0.0"  # inject your context here
        return callback(value, ctx)   # call the original callback
    return wrapper


for name, command in commands.items():
    app.add_typer(command)


@app.callback(invoke_without_command=True)
def main(
        ctx: typer.Context,
        version: Annotated[Optional[bool], typer.Option(
            "--version",
            "-v",
            callback=with_context(callbacks["version"]),
            is_eager=True
        )] = None
):
    pass


if __name__ == "__main__":
    app()
