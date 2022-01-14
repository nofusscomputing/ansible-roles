# Ansible Role fail2ban
This ansible role installs fail2ban on a debian host.

This ansible role is intended to be used as a dependency of other ansible roles. For example, if you would like to configure fail2ban, create an ansible role, with this role as a dependency and then create tasks in your role to configure fail2ban.


## Dependencies

- [data_setup](../data_setup)


## Variables

| Variable Name | Default Value | Description |
|:---|:---:|:---|
| `fail2ban_package_sha256` | _None_ | The sha256 hash of the downloaded package. |
| `version_fail2ban` | _None_ | This variable is the fail2ban version to install. See [releases](https://github.com/fail2ban/fail2ban/releases) for available version numbers |


## Workflow

1. export variable `directory_fail2ban_config` for other ansible role use.

1. download fail2ban deb package

1. if fail2ban is already installed, stop the fail2ban service

1. install the supplied version

1. start the fail2ban service.
