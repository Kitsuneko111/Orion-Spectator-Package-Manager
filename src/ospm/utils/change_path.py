import sys

import typer
import os
import subprocess
from pathlib import Path
from .easy_print import easy_print


def change_path(ctx: typer.Context, package):
    context_root = Path.cwd().resolve()
    intended_root = Path.home().joinpath("Another-Axiom/A2/Cameras/Behaviors")
    try:
        context_root.relative_to(intended_root)
    except ValueError:
        easy_print("[WARN]",
                   "Attempting to run future commands from folder not within the personal directory. Is this a mistake?")
    target = Path(package).resolve()
    if not target.exists():
        try:
            target.relative_to(context_root)
            confirmation = False
            if "yes" not in ctx.obj or not ctx.obj["yes"]:
                confirmation = typer.confirm("Do you wish to create this directory?")
            if confirmation or "yes" in ctx.obj and ctx.obj["yes"]:
                Path.mkdir(target, parents=True)
            else:
                return typer.Exit(code=1)
        except ValueError:
            easy_print("[ERROR]", f"Path does not exist: {target}")
            return typer.Exit(code=1)

    try:
        target.relative_to(context_root)
    except ValueError:
        easy_print("Attempting to move to folder that is not a subdirectory. Is this a mistake?",
                   "[WARN]")
    if target != context_root:
        shell_cmd = os.environ.get("SHELL", "cmd" if os.name == "nt" else "bash")
        print("Launching new Terminal.")
        print("Type `exit` to exit this terminal.")
        subprocess.run([shell_cmd, "echo"], cwd=target)
