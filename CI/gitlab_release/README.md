# Gitlab Release

> This gitlab job will only run from the development branch.

This CI job's workflow is:

1. updates the changelog from the commits
1. commit the changelog to git
1. adds a `git tag` to the changelog commit. 
1. pushes the change back to the repo
1. creates a git release from the `git tag`

The git tag and release title use [semantic versioning](https://semver.org/). for this job to function correctly a `.cz.yaml` is required in the root of the repository. this file contains the [commitizen](https://github.com/commitizen-tools/commitizen) config and the version details.
