import typer


def version_callback(value: bool, ctx: typer.Context):
    if value:
        print(f"OSPM is running version {ctx.obj["version"]}")
        raise typer.Exit()
