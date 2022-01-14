## v0.1.2 (2022-01-14)

### Bug Fixes

- **nginx**: [ed2d6172](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/ed2d6172c77d4c9b5662d4b59bef8469d5eed534) - ensure any config changes to logrotate trigger a restart of logrotate. [ [!6](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/6) ]
- **logrotate**: [262a1ac1](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/262a1ac19d878dc40134dbe364fa62c6d186b1fd) - incorrect name used in roles [ [!6](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/6) ]
- **nginx**: [f667b238](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/f667b2384240d5d3dbadec3b8c7d8f913bf264f2) - mount http directory within container so that files can be served if configured to. [ [#8](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/issues/8) [!10](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/10) ]

### Continious Integration

- **gitlab-ci**: [3c32c226](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/3c32c226d307ccf399421939d6d15655f4a81683) - update to latest commit '9cd94c124c8076f72cde698a52cad15dbbe4a576' [ [!10](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/10) ]

### Documentaton / Guides

- **readme**: [0007a896](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/0007a896cc7f88e6df9f3931d7c925a8419395ec) - fix link to point to correct role. [ [!6](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/6) ]
- **README**: [dd77a818](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/dd77a818675c6f3a1dcc059f1149e67a34f0be15) - added repo usage and explaination. [ [!10](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/10) ]

### Features

- **users_groups**: [7be070f5](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/commit/7be070f52e9114b960c0ebcecdc17ecf82b2f7ef) - added new role [ [#2](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/issues/2) [!10](https://gitlab.com/nofusscomputing/projects/ansible-roles/-/merge_requests/10) ]

## v0.1.2rc3 (2022-01-13)

### Bug Fixes

- **logrotate**: [ac1b17cc](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/ac1b17cc64127db3c27681417a595f1a0cd73576) - stop and start service as required. [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]
- **fail2ban**: [fa71d008](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/fa71d00858e09d18716ca545d2c1d9dc5d4888da) - removed when condition as it's not required [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]

### Code Refactor

- [82b2e220](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/82b2e22017d0fca05ac1ea83a3f551f01ed78a53) - code review suggestions
- [71b5a1e8](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/71b5a1e822253b51dd99578130ec86f7e0b238d6) - correct linting errors [ [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]

### Continious Integration

- **gitlab-ci**: [0943ede7](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/0943ede7e6fd1ef7184808c92f303b1433ccee03) - updated to latest commit on dev branch. [ [!6](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/6) ]
- **gitlab-ci**: [d1e9c72b](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/d1e9c72b8e56172182b199a2210dc6ac614bc4dd) - gitlab-ci.yml updated to use project import [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) ]

### Features

- **logrotate**: [96e73d6c](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/96e73d6c28bf1a806592f9ddaef1c304a066a631) - add a handler to restart the service so config can be loaded. [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]
- **nginx**: [1a2db8ba](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/1a2db8bab4cdd10953b4943135c87d83ec741765) - added nginx role [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [#7](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/7) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]
- **logrotate**: [8c6e8506](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/8c6e8506534e5c6b1801e2580fe0d098c7a77430) - added ansible role logrotate [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]
- **fail2ban**: [107b364a](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/107b364a7990454ff5118abc711523609215e0b1) - added fail2ban role [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]
- **data_setup**: [868c3391](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/868c33917b84a1f991a67be0c35fd4399ce69ae8) - created role data_setup for creating data directories for roles [ [#2](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/issues/2) [!9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/merge_requests/9) ]

## v0.1.2rc2 (2021-08-04)

### Continious Integration

- **git_push_mirror**: [22b65543](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/22b65543a6024e46dc9db6e9783322795b0414b7) - again fix git sync url. was missing '-roles'

## v0.1.2rc1 (2021-08-04)

### Continious Integration

- **git_push_mirror**: [2896a77e](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/2896a77ee6f93da1e19b52c1a997c1e033e58ab7) - Sync to the correct git repo

## v0.1.2rc0 (2021-08-04)

### Continious Integration

- **gitlab-ci**: [03b58120](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/03b5812077136bc720b95b72dc8d6c0bbe3726d7) - Use gitlab-ci gitlab_release
- **gitlab-ci**: [295fe5b1](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/295fe5b1dbf0923b4e456440ee88acacaaa8d8b3) - Update to use fixed ansible job
- **ansible**: [c96a5173](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/c96a517316a1c391abb17d8e376f16f3c0b6f48b) - Migrate to gitlab-ci ansible linting.
- **git_push_mirror**: [a5a6d3d7](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/a5a6d3d71e7112a195925f6f1ee79ec1ee40fda6) - User gitlab-ci job git_push_mirror
- **gitlab-ci**: [2221ae4f](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/2221ae4f22233008421356efa0eb55a596e64b86) - Migrate to gitlab-ci conventional_commits.
- **gitlab-ci**: [e4703e09](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/e4703e09a30a5945a186965f39940b548929b037) - Added gitlab-ci repo as submodule

### Documentaton / Guides

- **changelog**: [2c0ea4d1](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/2c0ea4d1ba6e2da59cfb15dc2e61cfb237412d66) - updated changelog to use the new format

## v0.1.1 (2021-08-02)

### Documentaton / Guides

- **contribution**: [17f94ec9](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/17f94ec9bb415596f162c88c814a037fae21e8d3) - Add contribution documentation

## v0.1.0 (2021-08-02)

### Continious Integration

- **gitlab_release**: [7b2f8751](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/7b2f875185fddaeda0553f8efba3ab6140d69608) - Add CI documentation for job
- **gitlab_release**: [426dd608](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/426dd608690a9992c5ab45077edbd773396d23f3) - Use Release cli command to create release
- **gitlab_release**: [dc8367df](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/dc8367df586ce1b3304566c41b07e2ee2b95374d) - construct the clone url with authentication details
- **gitlab_release**: [09003101](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/09003101b86a45fa700b1e969b229d605aeef274) - ensure correct apk commands used and python3 is installed
- **commitizen**: [ae5c04bd](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/ae5c04bd1ad0d32a3e4ca8e3e680ccf9f178fbf5) - Adjust fetching of MR from API to use CI_JOB_TOKEN
- **commitizen**: [df447598](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/df44759893f930468e48d21f30b669433718be07) - updated api var.
- **gitlab_release**: [fce91e09](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/fce91e098431e5cf7656aab8da72d464d1da8fab) - Added configuration for bumping version on merge to development
- **gitlab_release**: [d276ac76](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/d276ac76560722ce2a67f81041d00eaf5cd87175) - config for version bump and changelog generation

### Features

- **develop**: [f7a4d11c](https://gitlab.com/nofusscomputing/infrastructure/ansible-roles/-/commit/f7a4d11c81e6e2e99ce19dc1392aee566192107e) - development environment setup script develop.sh

## v0.0.1 (2021-08-01)
