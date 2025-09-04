import pathlib
from typing import Optional, Union, List

import typer
from typing_extensions import Annotated

try:
    from ..utils.package_types import Package, CameraPackage
except ImportError:
    # noinspection PyUnresolvedReferences
    from utils.package_types import Package, CameraPackage
try:
    from ..utils.easy_print import easy_print
except ImportError:
    # noinspection PyUnresolvedReferences
    from utils.easy_print import easy_print

install_app = typer.Typer()


@install_app.command("i", hidden=True)
@install_app.command("add", hidden=True)
@install_app.command()
def install(ctx: typer.Context,
            package: List[str] = [],  # Uses the NPM System
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
            all_deps: Annotated[Optional[bool], typer.Option("--all", "--all-deps", "--all-dependencies", "-a")] = False,
            save_all: Annotated[Optional[bool], typer.Option("--save-all", "--save-all-deps", "-A")] = False,
            save_optional: Annotated[Optional[bool], typer.Option("--save-optional", "--save-opt", "-O",
                                                                 help="Save the installed package(s) to the optional dependencies.")] = False,
            save_developmental: Annotated[Optional[bool], typer.Option("--save-developmental", "--save-dev", "-D",
                                                                       help="Save the installed package(s) to the developmental dependencies")] = False,
            save_injectable: Annotated[Optional[bool], typer.Option("--save-injectable", "--save-inj", "-I",
                                                                    help="Save the installed package(s) to the injectable dependencies.")] = False,
            target: Annotated[Optional[pathlib.Path], typer.Option("--target", "-t",
                                                                                            help="Specifies a directory to install the package into. Must follow spectator package conventions.")] = "",
            index: Annotated[Optional[str], typer.Option("--index", "--index-url", "-U",
                                                                         help="Use a custom url to search for the package in.\n"
                                                                              "Note: This is currently just a prefix and may not be validated.")] = "",
            extra_index: Annotated[Optional[List[str]], typer.Option("--extra-index", "--extra-index-url", "--extra",
                                                                               help = "If the index url fails, try this one instead")] = [],
            report: Annotated[Optional[bool], typer.Option("--report", "-R")] = False,
            dry_run: Annotated[Optional[bool], typer.Option("--dry-run", "--no-save", "-F")] = False,
            ignore_installed: Annotated[Optional[bool], typer.Option("--ignore-installed", "-G",
                                                                     help="Ignore currently installed packages, possibly (likely) breaking them.")] = False):
    """
    A Package is:
    a) A folder containing a package.json (defaults to current directory).
    b) A tar.gz containing (a).
    c) A url that resolves to (b).
    d) A `<name>@<version>` that is published on the OSPM Registry (WIP) containing (c).
    e) A `<name>@<tag>` that resolves to (d).
    f) A `<name>` that uses a `latest` tag satisfying (e).
    g) A `git` url that resolves to (a).

    Aliases: i, install, add
    """
    if package == []:
        easy_print(ctx, "Inferring package as current project", "[INFO]")
        package = "."
    for pack in package:
        resolve_package(pack)


def resolve_package(pack: str) -> Package | CameraPackage:
    try_path = pathlib.Path(pack)
    if try_path.is_dir():
        if try_path.joinpath("package.json").is_file():
            pass
