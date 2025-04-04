# Description
Purpose of this repository is to provide a template to use for new repositories using my preferred tooling and best practices.



# Preferred Tools
Github (over gitlab, bitbucket, Azure Devops) because it is more widespread and integrated

uv for python management (over poetry, conda, venv, rye, pyenv) seems to be the future of python management

Ruff for linting (over pylint) quicker

Just (over makefiles) simpler and more tailored for commandline shortcuts

Typer for commandline tools

Copier (over cookiecutter and github templates) for repository templates because it allows customisation and template updates

Dynaconf for easy configuration settings

Python for multi-purpose programming

Quarto for documentation (over sphinx) because easy-to-use and great documentation and features

# Quick start installation
## Pre-requisites
- powershell: windows or linux
- just: https://just.systems/man/en/
- uv: https://docs.astral.sh/uv/
- quarto: https://quarto.org/
- github cli: to create remote repository automatically

## Installation
Run this:

`uvx copier copy --trust git@github.com:actuaristai/template.git path/to/newfolder`

Optional flag
`--vcs-ref=branch_name` to use a specific branch