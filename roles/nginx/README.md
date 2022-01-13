# Ansible Role nginx
This ansible role installs nginx within a docker container. this role also contains logrotate configuration for the nginx logs and a jail for fail2ban.

This ansible role is intended to be used as a dependency of other ansible roles. For example, if you would like to configure nginx, create an ansible role, with this role as a dependency and then create tasks in your role to configure nginx.


## Dependencies

- [data_setup](../data_setup)

- [fail2ban](../logrotate)

- [logrotate](../logrotate)


## Variables

| Variable Name | Where to set | Default Value | Description |
|:---|:---:|:---:|:---|
| DOCKER_CONTAINER_NAME_NGINX | _role_ | _nginx_ | The name the docker container will be given. |
| DIRECTORY_NGINX_CONFIG_ROOT | _role_ | _{{ DIRECTORY_STRUCTURE_CONFIG }}/{{ DOCKER_CONTAINER_NAME_NGINX }}_ | Root directory for the docker contaner data. |
| DIRECTORY_NGINX_CONFD | _role_ | _DIRECTORY_STRUCTURE_CONFIG }}/{{ DOCKER_CONTAINER_NAME_NGINX }}/conf.d_ | The nginx conf.d directory. |
| DIRECTORY_NGINX_HTTP | _role_ | _{{ DIRECTORY_STRUCTURE_CONFIG }}/{{ DOCKER_CONTAINER_NAME_NGINX }}/http_ | The nginx http directory. You can place your file for http within this directory. |
| DIRECTORY_NGINX_SSL | _role_ | _{{ DIRECTORY_STRUCTURE_DATA }}/{{ DOCKER_CONTAINER_NAME_NGINX }}/ssl_ | The directory for SSL Certificates |
| DIRECTORY_NGINX_LOGS | _role_ | _{{ DIRECTORY_STRUCTURE_LOGS }}/{{ DOCKER_CONTAINER_NAME_NGINX }}_ | The nginx log directory. |
| DOCKER_CONTAINER_NGINX_CPU_SET | _role_ | _0:3_ | Which CPUs the docker container will use. |
| DOCKER_CONTAINER_NGINX_MEMORY | _role_ | _0_ | The allocated memory for the docker container. |
| DOCKER_CONTAINER_NGINX_EXPOSED_PORTS | _role_ | _[80, 443]_ | The ports to expose to other docker containers. |
| DOCKER_CONTAINER_NGINX_PUBLISHED_PORTS | _role_ | _None_ | **_Optional_** The ports to publically make available from the docker container. |
| DOCKER_CONTAINER_USER_NGINX | _role_ | _{{ DOCKER_CONTAINER_NAME_NGINX }}"_ | **_Mandatory_** The system user and group to create for the data directories. |
| DOCKER_IMAGE_NGINX | _globally_ | _nginx"_ | The docker image to use for the container. |
| DOCKER_IMAGE_NGINX_TAG | _globally_ | _None_ | **_Mandatory_** The docker image tag to use for the container. |
| DOCKER_NETWORK_NGINX | _globally_ | _{{ DOCKER_CONTAINER_NAME_NGINX }}"_ | The name of the docker network to create. |


## Workflow

1. Check if already installed

1. create the user within the operating system.

1. create the group within the operating system.

1. pull the docker image

1. start the docker container

1. Add nginx default config

1. Add logrotate configuration

1. Add fail2ban jail
