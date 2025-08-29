import typer

lock_app = typer.Typer()


@lock_app.command()
def lock():
    raise NotImplementedError()
