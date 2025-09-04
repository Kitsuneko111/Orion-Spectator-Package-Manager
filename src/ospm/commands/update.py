import typer

update_app = typer.Typer()


@update_app.command("u", hidden=True)
@update_app.command("up", hidden=True)
@update_app.command("upgrade", hidden=True)
@update_app.command()
def update():
    """
    Aliases: u, up, upgrade, update
    """
    raise NotImplementedError()
