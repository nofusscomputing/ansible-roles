# Ansible Role Node Red
This ansible role installs Node Red within a docker container. ~~this role also contains logrotate configuration for the nginx logs and a jail for fail2ban~~.

~~This ansible role is intended to be used as a dependency of other ansible roles. For example, if you would like to configure nginx, create an ansible role, with this role as a dependency and then create tasks in your role to configure nginx.~~


## Dependencies

- [data_setup](../data_setup)

- ~~[fail2ban](../fail2ban)~~

- ~~[logrotate](../logrotate)~~


## Variables

| Variable Name | Where to set | Default Value | Description |
|:---|:---:|:---:|:---|
| docker_container_name_nodered | _role_ | _home_assistant_ | The name the docker container will be given. |
| docker_nodered_config_root | _role_ | _{{ directory_structure_config }}/{{ docker_container_name_nodered }}_ | Root directory for the docker contaner data. |
| docker_nodered_logs | _role_ | _{{ directory_structure_logs }}/{{ docker_container_name_nginx }}_ | The nginx log directory. |
| docker_container_nodered_cpu_set | _role_ | _0:3_ | Which CPUs the docker container will use. |
| docker_container_nodered_memory | _role_ | _0_ | The allocated memory for the docker container. |
| docker_container_nodered_exposed_ports | _role_ | _[1880]_ | The ports to expose to other docker containers. |
| docker_container_nodered_published_ports | _role_ | _None_ | **_Optional_** The ports to publically make available from the docker container. |
| docker_container_user_nodered | _role_ | _{{ docker_container_name_nodered }}"_ | **_Mandatory_** The system user and group to create for the data directories. |
| docker_image_nodered | _globally_ | _nodered/home-assistant_ | The docker image to use for the container. |
| docker_image_nginx_tag | _globally_ | _None_ | **_Mandatory_** The docker image tag to use for the container. |
| docker_network_nodered | _globally_ | _{{ docker_container_name_nodered }}"_ | The name of the docker network to create. |


## Workflow

1. Check if already installed

1. create the user within the operating system.

1. create the group within the operating system.

1. pull the docker image

1. start the docker container

1. Add nodered default config

1. ~~Add logrotate configuration~~

1. ~~Add fail2ban jail~~
