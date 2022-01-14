# No Fuss Computing Ansible Roles

<div align="center">

![Project Status - Active](https://img.shields.io/badge/Project%20Status-Active-green?logo=gitlab&style=plastic)

[![Gitlab build status - stable](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build%20%5B%20Stable%20%5D&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28204898%2Fpipelines%3Fref%3Dmaster&logo=gitlab&style=plastic)](https://gitlab.com/nofusscomputing/projects/ansible-roles) [![Gitlab build status - development](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build%20[%20Development%20]&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28204898%2Fpipelines%3Fref%3Ddevelopment&logo=gitlab&style=plastic)](https://gitlab.com/nofusscomputing/projects/ansible-roles) [![Open Issues](https://img.shields.io/badge/dynamic/json?color=ff782e&logo=gitlab&style=plastic&label=Open%20Issues&query=%24.statistics.counts.opened&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28204898%2Fissues_statistics)](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/issues)

</div>

This repository is hosted on [gitlab.com](https://gitlab.com/nofusscomputing/projects/ansible-roles) and has a read-only copy hosted on [github.com](https://github.com/NoFussComputing/ansible-roles).

links:
- [Issues](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/issues)

- [Merge Requests (Pull Requests)](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests)


This repository contains ansible roles. Within each role directory, you will find a readme that explains the role in question.

Each of the roles are designed in a way that they can be used as dependencies for your own roles. They are also designed to run them over and over so that you can determine if anything has changed.

It is possible to use tags for our roles. This will enable you to do a staging prior to a deployment. The available tags are as follows:

- `prepare` _tasks that require work, doesn't make any changes. example: build docker image, pull docker image_

- `configure` _add any configuration files, users, groups etc. Does make changes_

- `install` _install the feature of the role_

- `remove` _uninstall the feature of the role. Does not remove items added by the role_

- `clean` _removes all items added by the role._


## Branches
**master:** Considered stable. Every merge request creates a release.

**development:** Considered unstable _(might change)._ any releases on this branch are release-candidates, prefixed as `rc*`.

| :interrobang: Release Versioning |
|:---|
| _we use semantic versioning._<br><br>_Any change we make that will break an existing setup, we increase the `major` number within the version. i.e. 1.0.0 -> 2.0.0_ |

## Using our Ansible roles
As this forms part of your configuration management, it is intended that you would add this repository to your ansible root folder, with an update to your `ansible.cfg` _(roles=./roles:./ansible-roles/roles)_, you can use our roles alongside your roles.

If your ansible roles are not part of a git repository _(why?)_ you can just clone this repo to the root directory of your ansible roles and update `ansible.cfg`.

For those who have thier ansible roles directory as part of a git repo, it is suggested to add this repository as a sub module. Using this option enables your git history to track what commit of our repository you are using. We encourage keeping the sub-module updated to a git tag for stability.

To utilise our role create your own role, and include our role as a dependency. As our roles will require you to configure them to suit your environment. For example, create a role `{rolename}_configuration` then include `{rolename}` as a dependency of the created role.

## Changelog
The master changelog is available in the [repo](https://gitlab.com/nofusscomputing/projects/ansible-roles/CHANGELOG.md). Every time we create a release including for alpha releases, the changelog is updated.

## Contributing
All contributions for this project must conducted from [Gitlab](https://gitlab.com/nofusscomputing/projects/ansible-roles).

For further details on contributing please refer to the [contribution guide](https://gitlab.com/nofusscomputing/projects/ansible-roles/CONTRIBUTING.md).


## Other

This repo is release under this [license](https://gitlab.com/nofusscomputing/projects/ansible-roles/LICENSE)
