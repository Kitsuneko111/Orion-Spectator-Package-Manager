import typer

list_app = typer.Typer()


@list_app.command("l")
@list_app.command("list")
def list_c():
    """
    Aliases: l, list
    """
    raise NotImplementedError()
