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
