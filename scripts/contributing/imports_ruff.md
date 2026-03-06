## Import order

Order of imports is enforced by [ruff](https://docs.astral.sh/ruff/) **linter**. The [imports can be automatically sorted](https://docs.astral.sh/ruff/formatter/#sorting-imports) by running:

```bash
ruff check --select I --fix
ruff format
```

As for formatting, we advise to use the [Ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) or [a Git hook](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks) to sort imports automatically when saving.

Configuration can be found in `pyproject.toml` under `[tool.ruff.lint.isort]` sections.
