# Ansible Role Users Groups
This ansible role will check existing groups and users against a supplied list of expected groups/users and remove additional groups/users. If the user or group is missing, will add them.


## Dependencies

- **_None_**


## Variables

| Variable Name | Where to set | Default Value | Description |
|:---|:---:|:---:|:---|
| `groups_host` | _host_vars_ | _None_ | A list of groups to add to the host. |
| `users_host` | _host_vars_ | _None_ | A list of users to add to the host |


## Workflow

1. Fetch existing groups

1. if `groups_host` defined, remove groups not in list `groups_host`

1. if `groups_host` defined, add the missing groups

1. fetch existing users

1. if `users_host` defined, remove users not in list `users_host`

1. if `users_host` defined, add missing users _(does not add passswords)_
