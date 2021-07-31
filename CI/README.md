# CI Folder

This folder is related to the CI/Build. You can safely delete it, if you have cloned the repository.

## Structure

Each sub-folder is related to an individual feature/funtion of the CI system. 
If a feature/function is not required, then delete the sub-folder.

To link the feature to CI so that it is used add the following to the root `.gitlab-ci.yml` file.

``` yaml
include:
  - local: CI/{sub-folder}/.gitlab-ci.yml
``` 

with `{sub-folder}` being the name of the sub-folder to include. 
