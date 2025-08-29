import pathlib
import toml

pyproject_file = pathlib.Path(__file__).parent.parent.parent.parent / "pyproject.toml"

data = toml.load(pyproject_file)
version = data["project"]["version"]
