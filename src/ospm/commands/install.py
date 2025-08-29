import typer

install_app = typer.Typer()


@install_app.command("i")
@install_app.command("add")
@install_app.command()
def install():
    """
    Aliases: i, install, add
    """
    raise NotImplementedError()
