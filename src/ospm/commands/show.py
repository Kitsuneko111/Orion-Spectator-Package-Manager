import typer

show_app = typer.Typer()


@show_app.command("s", hidden=True)
@show_app.command()
def show():
    """
    Aliases: s, show
    """
    raise NotImplementedError()
