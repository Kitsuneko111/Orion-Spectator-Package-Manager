import typer

package_app = typer.Typer()


@package_app.command("p", hidden=True)
@package_app.command()
def package():
    """
    Aliases: p, package
    """
    raise NotImplementedError()
