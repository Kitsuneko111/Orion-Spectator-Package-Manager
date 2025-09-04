from .check import check_app
from .docs import docs_app
from .download import download_app
from .freeze import freeze_app
from .init import init_app
from .install import install_app
from .list import list_app
from .lock import lock_app
from .package import package_app
from .show import show_app
from .uninstall import uninstall_app
from .update import update_app


commands = {
    "check": check_app,
    "docs": docs_app,
    "download": download_app,
    "freeze": freeze_app,
    "init": init_app,
    "install": install_app,
    "list": list_app,
    "lock": lock_app,
    "package": package_app,
    "show": show_app,
    "uninstall": uninstall_app,
    "update": update_app
}
