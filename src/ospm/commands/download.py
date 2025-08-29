import typer

download_app = typer.Typer()


@download_app.command("d")
@download_app.command("dl")
@download_app.command()
def download():
    """
    Aliases: d, dl, download
    """
    raise NotImplementedError()
