# Ansible Role data_setup
This role sets up the data directories for use by other ansible roles.

The purpose of the directories are as follows:

- `Backup` _The location for backups to be saved. Sub-directories for each role_

- `Config` _location  role configuration files. Roles should create a sub-directory for each role. Data in this location is not intended to be part of the backup process. As files placed here are created by the ansible role_

- `Data` _Location for roles data files. Sub-directory for each role. This location is included the backup process_

- `logs` _Location for role log files. Sub-directory for each role. This location is included the backup process_

This ansible role is intended to be a dependency of other ansible roles. Each sub folder that this role creates, is where your ansible roles will create there sub directories and give the appropriate ownership and permissions.


## Dependencies

- None

## Variables

| Variable Name | Default Value | Description |
|:---|:---:|:---|
| `directory_structure_root` | _None_ | **_Mandatory_**This variable is a the root directory of where you would like to create the data directories. i.e. `/data` |
| `directory_structure_backup` | _`{{ directory_structure_root}}/backup`_ | This variable is a the root directory of where you would like to create the data directories. i.e. `/data` |
| `directory_structure_config` | _`{{ directory_structure_root}}/config`_ | This variable is a the root directory of where you would like to create the data directories. i.e. `/data` |
| `directory_structure_data` | _`{{ directory_structure_root}}/data`_ | This variable is a the root directory of where you would like to create the data directories. i.e. `/data` |
| `directory_structure_logs` | _`{{ directory_structure_root}}/logs`_ | This variable is a the root directory of where you would like to create the data directories. i.e. `/data` |



## Workflow

> All directories are given ownership of root and mask of `0755
`
1. Creates root directory

1. Creates `{rootdir}\backup` directory

1. Creates `{rootdir}\config` directory

1. Creates `{rootdir}\data` directory

1. Creates `{rootdir}\config` directory


