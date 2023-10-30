# Welcome to python_project_template 👋

Python project template with tests, docs, and minimal CI.

## Usage

Install [cookiecutter][cookiecutter] following the [official instructions][cookiecutter-installation], then use this project as a template

```bash
cookiecutter https://github.com/nickuzmenkov/python_project_template.git
```

You will then be prompted to fill in the project name, description and other project-related metadata.

Once you are done, you can optionally add up-to-date dependencies for testing and documentation purposes

```bash
poetry add --group tests autoflake isort black flake8 pylint mypy pytest pytest-cov
poetry add --group docs mkdocs mkdocs-material
```

# Authors

- Nick Kuzmenkov

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-installation]: https://cookiecutter.readthedocs.io/en/latest/installation.html
