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
