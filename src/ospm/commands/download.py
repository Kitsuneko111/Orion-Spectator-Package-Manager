import typer

download_app = typer.Typer()


@download_app.command("d", hidden=True)
@download_app.command("dl", hidden=True)
@download_app.command()
def download():
    """
    Aliases: d, dl, download
    """
    raise NotImplementedError()
