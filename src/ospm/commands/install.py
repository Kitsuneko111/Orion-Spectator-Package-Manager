import os
import pathlib
from typing import Optional, Union, List

import typer
from typing_extensions import Annotated

from pydantic import HttpUrl

install_app = typer.Typer()


@install_app.command("i")
@install_app.command("add")
@install_app.command()
def install(ctx: typer.Context,
            package: Annotated[Optional[List[str]], typer.Argument()] = "",
            optionals: Annotated[Optional[bool], typer.Option("--optionals", "--optional", "--optional-deps", "--opt", "--opt-deps", "-o",
                                                              help="Installs dependencies from the optional dependencies category of the package to install or current package if none is specified.")] = False,
            developmental: Annotated[Optional[bool], typer.Option("--developmentals", "--developmental", "--developmental-deps", "--dev", "--dev-deps", "-d",
                                                                  help="Installs dependencies from the development dependencies category of the package to install or current package if none is specified.")] = False,
            injectables: Annotated[Optional[bool], typer.Option("--injectables", "--injected", "--injectable-deps", "--injected-deps", "--inj", "--inj-deps", "-i",
                                                                help="Installs dependencies from the injectablee dependencies category of the package to install or current package if none is specified."),] = False,
            upgrade: Annotated[Optional[bool], typer.Option("--upgrade", "--update", "-u",
                                                            help="Checks for updates of all specified packages")] = False,
            no_deps: Annotated[Optional[bool], typer.Option("--no-deps", "--no-reqs", "--solo", "-s",
                                                            help="Don't install the normal dependencies.\n"
                                                                 "Can be used alongside -o, -d or -i to only install those dependencies.")] = False,
            target: Annotated[Optional[Union[str, os.PathLike, pathlib.Path]], typer.Option("--target", "-t",
                                                                                            help="Specifies a directory to install the package into. Must follow spectator package conventions.")] = "",
            index: Annotated[Optional[Union[str, HttpUrl]], typer.Option("--index", "--index-url", "-I",
                                                                         help="Use a custom url to search for the package in.\n"
                                                                              "Note: This is currently just a prefix and may not be validated.")] = "",
            extra_index: Annotated[Optional[List[Union[str, HttpUrl]]], typer.Option("--extra-index", "--extra-index-url", "--extra",
                                                                               help = "If the index url fails, try this one instead")] = "",
            report: Annotated[Optional[bool], typer.Option("--report", "-R")] = False,
            dry_run: Annotated[Optional[bool], typer.Option("--dry-run", "-F")] = False,
            ignore_installed: Annotated[Optional[bool], typer.Option("--ignore-installed", "-I",
                                                                     help="Ignore currently installed packages, possibly (likely) breaking them.")] = False):
    """
    Aliases: i, install, add
    """
    raise NotImplementedError()
