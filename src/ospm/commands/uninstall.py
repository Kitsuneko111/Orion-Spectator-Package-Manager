import typer

uninstall_app = typer.Typer()


@uninstall_app.command("un")
@uninstall_app.command("unin")
@uninstall_app.command("rem")
@uninstall_app.command("remove")
@uninstall_app.command()
def uninstall():
    """
    Aliases: un, unin, uninstall, rem, remove
    """
    raise NotImplementedError()
