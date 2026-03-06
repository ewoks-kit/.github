## Linting

[ruff](https://docs.astral.sh/ruff/) is used to lint the code. The linting is equivalent to [flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8) linting.

[Configuration](https://docs.astral.sh/ruff/configuration/) can be changed in `pyproject.toml` but the default configuration is compatible with black so that changes should not be needed. If needed, linting errors can be [ignored inline by adding comments](https://docs.astral.sh/ruff/linter/#line-level) (e.g.`# noqa: E123`).
