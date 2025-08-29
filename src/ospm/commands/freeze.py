import typer

freeze_app = typer.Typer()


@freeze_app.command("f")
@freeze_app.command("fr")
@freeze_app.command()
def freeze():
    """
    Aliases: f, fr, freeze
    """
    raise NotImplementedError()
