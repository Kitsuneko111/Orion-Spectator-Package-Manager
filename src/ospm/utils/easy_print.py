from typing import Optional

import click
import typer
from rich import print

verbosity_lookup = {
    "[INFO]": "[bright_cyan][INFO][/bright_cyan] ",
    "[LOG]": "[blue][LOG][/blue] ",
    "[WARN]": "[yellow][WARN][/yellow] ",
    "[ERROR]": "[red][ERROR][/red] ",
    "[DEBUG]": "[DEBUG] "
}


def easy_print(*args, **kwargs):
    """
    :param args:
    If an argument is a verbosity, apply that verbosity to the logs otherwise use [LOG]
    If an argument is an instance of click.core.Context use that as context, otherwise assume normal
    :param kwargs:
    Passes all other args and kwargs to rich print
    """
    context: Optional[typer.Context] = None
    verbosity = ""
    new_args = []
    for arg in args:
        if isinstance(arg, click.core.Context):
            context = arg
        elif arg == "[INFO]":
            verbosity = "[INFO]"
        elif arg == "[LOG]":
            verbosity = "[LOG]"
        elif arg == "[WARN]":
            verbosity = "[WARN]"
        elif arg == "[ERROR]":
            verbosity = "[ERROR]"
        elif arg == "[DEBUG]":
            verbosity = "[DEBUG]"
        else:
            new_args.append(arg)

    if verbosity == "":
        verbosity = "[LOG]"
    if context is not None:
        if verbosity in ["[INFO]", "[DEBUG]"] and "verbose" in context.obj and context.obj["verbose"] is not True:
            return
        if verbosity in ["[INFO]", "[LOG]", "[DEBUG]", "[WARN]"] and "quiet" in context.obj and context.obj["quiet"] is True:
            return
    new_args[0] = verbosity_lookup[verbosity]+new_args[0]
    print(*new_args, **kwargs)
