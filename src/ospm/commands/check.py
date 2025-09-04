import typer

check_app = typer.Typer()


@check_app.command("ch", hidden=True)
@check_app.command()
def check():
    """
    Aliases: ch, check
    """
    raise NotImplementedError()
