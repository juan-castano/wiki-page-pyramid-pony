# Wiki page using PonyORM
### Repo based on Pyramid framework tutorial for Python lang.

Wiki Page
=========

Getting Started
---------------

- Change directory into your newly created project.

    cd wiki_page

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
