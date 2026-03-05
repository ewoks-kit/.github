from pathlib import Path

if __name__ == "__main__":

    thisdir = Path(__file__).parent

    sections = thisdir / "contributing"

    GETTING_STARTED = (sections / "getting_started.md").read_text()
    TESTING = (sections / "testing.md").read_text()
    WRITE_DOCS = (sections / "write_docs.md").read_text()
    BUILD_DOCS = (sections / "build_docs.md").read_text()
    RELEASING = (sections / "releasing.md").read_text()

    FORMATTING_BLACK = (sections / "formatting_black.md").read_text()
    LINTING_FLAKE8 = (sections / "linting_flake8.md").read_text()
    IMPORTS_ISORT = (sections / "imports_isort.md").read_text()

    FORMATTING_RUFF = (sections / "formatting_ruff.md").read_text()
    LINTING_RUFF = (sections / "linting_ruff.md").read_text()
    IMPORTS_RUFF = (sections / "imports_ruff.md").read_text()

    default_contributing = (
        GETTING_STARTED
        + "\n"
        + FORMATTING_BLACK
        + "\n"
        + LINTING_FLAKE8
        + "\n"
        + IMPORTS_ISORT
        + "\n"
        + TESTING
        + "\n"
        + WRITE_DOCS
        + "\n"
        + BUILD_DOCS
        + "\n"
        + RELEASING
    )

    ruff_contributing = (
        GETTING_STARTED
        + "\n"
        + FORMATTING_RUFF
        + "\n"
        + LINTING_RUFF
        + "\n"
        + IMPORTS_RUFF
        + "\n"
        + TESTING
        + "\n"
        + WRITE_DOCS
        + "\n"
        + BUILD_DOCS
        + "\n"
        + RELEASING
    )

    (thisdir.parent / "shared" / "CONTRIBUTING.md").write_text(default_contributing)
    (thisdir.parent / "shared" / "CONTRIBUTING_ruff.md").write_text(ruff_contributing)
