import typer

check_app = typer.Typer()


@check_app.command("ch")
@check_app.command()
def check():
    """
    Aliases: ch, check
    """
    raise NotImplementedError()
