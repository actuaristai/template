"""Use Typer to run different scripts to do project chores.

Usage: uv run python project_management.py --help
Examples:
uv run python project_management.py bump-version 0.1.0
"""
from pathlib import Path

import toml
import typer

app = typer.Typer()


@app.command()
def bump_version(new_version: str) -> None:
    """Bump version using CLI (used in makefile)."""
    file_path = Path('pyproject.toml')

    with Path.open(file_path) as f:
        pyproject_toml = toml.load(f)

    pyproject_toml['project']['version'] = new_version

    with Path.open(file_path, 'w') as f:
        toml.dump(pyproject_toml, f)


if __name__ == '__main__':
    app()
