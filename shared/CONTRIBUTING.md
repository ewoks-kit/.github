## Getting started

Requirements are listed in `pyproject.toml` and can be installed with

```bash
pip install .[dev]
```

## Formatting

All code must be formatted with [black](https://black.readthedocs.io/en/stable) latest version or the CI will break. Editor integration such as [Black VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) or [Git hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks) can be set-up for automatic formatting.

The configuration can be found in `pyproject.toml`. 

## Linting

[flake8](https://flake8.pycqa.org/en/latest/index.html) is used to lint the code. 

The configuration is located in `.flake8`. It is written specifically to be compatible with black so that changes should not be needed. If needed, linting errors can be [ignored inline by adding comments](https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors) (e.g.`# noqa: E123`).

## Import order

Order of imports is enforced by [isort](https://pycqa.github.io/isort/). Same as for black, editor extensions such as [isort VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) can be used to sort imports automatically when saving.

The configuration in `pyproject.toml` is made to be [compatible with black](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html). 

## Testing

Tests make use [pytest](https://docs.pytest.org/en/stable/index.html) and can be run as follows

```bash
pytest .
```

Testing an installed project is done like this

```bash
pytest --pyargs <project_name>
```

## Write documentation

The documentation is composed of RST files located in `doc`. You can look at the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for information on how to write RST files.

If a new file is created, don't forget to reference it in one of the `toctree` directive.

## Build documentation

The documentation is built with [Sphinx](https://www.sphinx-doc.org/en/master/) that generates HTML pages out of the RST files. The configuration of Sphinx is in `doc/conf.py`.

Requirements (including Sphinx) can be installed with

```bash
pip install .[doc]
```

Then, build the documentation with

```bash
sphinx-build doc build/sphinx/html -E -a
```

The generated HTML pages will be available in `build/sphinx/html`. You can browse them by opening `build/sphinx/html/index.html` in your browser.

When rebuilding the documentation, don't forget to remove generated files to have a fresh `autodoc` documentation:

```bash
rm -rf doc/_generated/; sphinx-build doc build/sphinx/html -E -a
```

## Releasing

1. Checkout `main` and verify that it is up to date with the server and that your working tree is clean.

1. Add the [changes](https://changelog.md) to `CHANGELOG.md` under a version number that matches the
   [regex pattern](https://regex101.com/r/Ly7O1x/3/) provided by the [semantic versioning](https://semver.org)
   guidelines. For example the lifecycle of a single version could be

   ```
   1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-beta < 1.0.0-beta.1 < 1.0.0-rc.1 < 1.0.0
   ```

1. Change the version number in `<project>/pyproject.toml` to the version number put in the CHANGELOG.

1. Push your changes to a branch and create a MR to merge your changes in `main`.

1. Deploy the project using one of the two methods below:

   - Deploy through CI jobs (recommended)

      Launch the `Release` pipeline can manually confirm the steps for 
      deployment on [pypi](https://pypi.org) and [testpypi](https://test.pypi.org)
      When the `pypi` job succeeds a git tag for the version will be added to the repository.

   - Deploy manually from the terminal with `build` and `twine`

      ```bash
      rm -rf dist
      pip install build
      python3 -m build -s
      twine upload -r testpypi dist/*
      twine upload -r pypi dist/*
      ```

1. A git tag for the version is created automatically when deploying through the `pypi` CI job. Manual deployment however
   requires manual tagging

   ```bash
   git tag v1.2.3
   git push && git push --tags
   ```
