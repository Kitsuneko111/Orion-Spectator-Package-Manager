from typing import Optional
from typing_extensions import Annotated
import typer

from gui.gui import run_gui
from utils.change_path import change_path
from utils.generate_version import version
from utils.easy_print import easy_print

from commands import commands
from callbacks import callbacks

app = typer.Typer(rich_markup_mode="markdown")


# Pre-injection wrapper for any callback
# Yes I gave up and used AI here, sue me it's a hard injection to do
def with_context(callback):
    def wrapper(value, ctx: typer.Context):
        if ctx.obj is None:
            ctx.obj = {}
        ctx.obj["version"] = version  # inject your context here
        return callback(value, ctx)   # call the original callback
    return wrapper


for name, command in commands.items():
    app.add_typer(command)


@app.callback(invoke_without_command=True)
def main(
        ctx: typer.Context,
        package: Annotated[Optional[str], typer.Option("--package", "-p")] = "",
        version: Annotated[Optional[bool], typer.Option(
            "--version",
            "-v",
            callback=with_context(callbacks["version"]),
            is_eager=True
        )] = None,
        verbose: Annotated[Optional[bool], typer.Option(help="Adds extra logging")] = False,
        quiet: Annotated[Optional[bool], typer.Option("--quiet", "-q",
                                                      help="Lessens the output logs (overrides --verbose)")] = False,
        yes: Annotated[Optional[bool], typer.Option("--yes", "-y")] = False,
        gui: Annotated[Optional[bool], typer.Option()] = False
):
    if verbose:
        ctx.obj["verbose"] = True
        easy_print(ctx, "Setting up context", "[INFO]")
    if quiet:
        ctx.obj["quiet"] = True
    if yes:
        ctx.obj["yes"] = True
    if gui:
        if verbose:
            easy_print(ctx, "Starting GUI", "[INFO]")
        run_gui()

    change_path(ctx, package)


if __name__ == "__main__":
    app()
