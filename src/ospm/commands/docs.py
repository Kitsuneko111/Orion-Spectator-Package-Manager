import typer

docs_app = typer.Typer()


@docs_app.command()
def docs():
    raise NotImplementedError()
