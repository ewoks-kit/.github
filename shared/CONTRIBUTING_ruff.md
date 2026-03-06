## Getting started

Requirements are listed in `pyproject.toml` and can be installed with

```bash
pip install [--user] .[dev]
```

## Formatting

[ruff](https://docs.astral.sh/ruff/) is used to format the code. It gives formatting equivalent to [black](https://docs.astral.sh/ruff/faq/#how-does-ruffs-formatter-compare-to-black).

Editor integration such as [Ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) or [Git hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks) can be set-up for automatic formatting.

The configuration can be found in `pyproject.toml` under `[tool.ruff.format]` sections.

## Linting

[ruff](https://docs.astral.sh/ruff/) is used to lint the code. The linting is equivalent to [flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8) linting.

[Configuration](https://docs.astral.sh/ruff/configuration/) can be changed in `pyproject.toml` but the default configuration is compatible with black so that changes should not be needed. If needed, linting errors can be [ignored inline by adding comments](https://docs.astral.sh/ruff/linter/#line-level) (e.g.`# noqa: E123`).

## Import order

Order of imports is enforced by [ruff](https://docs.astral.sh/ruff/) **linter**. The [imports can be automatically sorted](https://docs.astral.sh/ruff/formatter/#sorting-imports) by running:

```bash
ruff check --select I --fix
ruff format
```

As for formatting, we advise to use the [Ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) or [a Git hook](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks) to sort imports automatically when saving.

Configuration can be found in `pyproject.toml` under `[tool.ruff.lint.isort]` sections.

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

      Once the tests have passed on `main`, CI jobs for deployment on [pypi](https://pypi.org) and [testpypi](https://test.pypi.org)
      will be available in the CI pipeline page. Launching these jobs manually will trigger the deployment on the corresponding
      python package index. In case of the `pypi` job a git tag for the version will be added to the repository.

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

   Release notes can be added in the `Tags` page of the gitlab repository.
