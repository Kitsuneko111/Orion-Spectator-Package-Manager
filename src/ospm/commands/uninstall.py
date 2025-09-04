import typer

uninstall_app = typer.Typer()


@uninstall_app.command("un", hidden=True)
@uninstall_app.command("unin", hidden=True)
@uninstall_app.command("rem", hidden=True)
@uninstall_app.command("remove", hidden=True)
@uninstall_app.command()
def uninstall():
    """
    Aliases: un, unin, uninstall, rem, remove
    """
    raise NotImplementedError()
