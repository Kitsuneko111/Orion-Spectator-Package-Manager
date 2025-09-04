import typer
try:
    from ..utils.change_path import change_path
except ImportError:
    # noinspection PyUnresolvedReferences
    from utils.change_path import change_path

goto_app = typer.Typer()


@goto_app.command("explore", hidden=True)
@goto_app.command("manage", hidden=True)
@goto_app.command("e", hidden=True)
@goto_app.command("m", hidden=True)
@goto_app.command("g", hidden=True)
@goto_app.command()
def goto(ctx: typer.Context, package: str):
    """
    Aliases: e, m, g, explore, manage, goto
    """
    change_path(ctx, package)
