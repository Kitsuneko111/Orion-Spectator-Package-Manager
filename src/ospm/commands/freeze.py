import typer

freeze_app = typer.Typer()


@freeze_app.command("f", hidden=True)
@freeze_app.command("fr", hidden=True)
@freeze_app.command()
def freeze():
    """
    Aliases: f, fr, freeze
    """
    raise NotImplementedError()
