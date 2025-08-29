import typer

update_app = typer.Typer()


@update_app.command("u")
@update_app.command("up")
@update_app.command("upgrade")
@update_app.command()
def update():
    """
    Aliases: u, up, upgrade, update
    """
    raise NotImplementedError()
