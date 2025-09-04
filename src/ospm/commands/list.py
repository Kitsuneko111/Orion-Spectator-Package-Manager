import typer

list_app = typer.Typer()


@list_app.command("l", hidden=True)
@list_app.command("li", hidden=True)
@list_app.command("list")
def list_c():
    """
    Aliases: l, list
    """
    raise NotImplementedError()
