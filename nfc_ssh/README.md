# ssh Ansible Role


This provides a method to install and configure an ssh server on a host. There is also an option to configure fail2ban and the firewall for sshd. SSH Host certificate CA signing is also provided as an option.

<div align="center">

## Role Details

| Item| Value | Description |
|:---|:---:|:---|
| Dependent Roles | _[nfc_common](../common/index.md)_ | Mandatory. Required for the use of application install |
|  | _[nfc_firewall](../firewall/index.md)_ | Optional role if you wish to configure the firewall and fail2ban for this role |
| Gate Variables | `nfc_ssh_install_sshd` | _Boolean._ Install and configure OpenSSH Server. |
| | `nfc_firewall_install_fail2ban`  | _See [nfc_firewall role](../firewall/index.md)_|
| | `nfc_firewall_install_firewall`  | _See [nfc_firewall role](../firewall/index.md)_|
| | `nfc_ssh_sign_key_with_ca`  | _Boolean._ Sign the host ssh public key with the specified host Certificate Authority Key. |
| Idempotent | _Yes_ |  |
| Stats Available | _Yes_ | Available under yaml path `nfc_ssh` for this role and `nfc_firewall` if option to configure sshd firewall/fail2ban |
| Tags | `check` | |
|  | `configure` | Specifying this option will configure an existing sshd installation|
|  | `install` | |
|  | `renew` | Force recreation/renewal of host SSH keys. |

</div>


Role flow:

- role to generate host certs
- role to sign host certs with hos ca
- user ca cert deployed to host
- certs deployed
- role installed

configure:

- check cert validity
- expired, recreate certs and sign
- restart ssh server

## Artifacts / Stats

This role does generate Ansible Artifiacts using the `stats` module. Available stats are:

```json
{
    "nfc_ssh": {
        "sshd": {
            "configuration": 
                "{ dictionary of the nfc_ssh_configuration variable }",
            "configured": true,
            "enabled": true,
            "host_key_details": {
                "certificate_details_first_pass": "/etc/ssh/ssh_host_ed25519_key-cert.pub:
        Type: ssh-ed25519-cert-v01@openssh.com host certificate
        Public key: ED25519-CERT SHA256:p3hdvH7EBrRfA2yQPiaFnP29NFSxj+mtcjaTrjVNAs8
        Signing CA: ED25519 SHA256:jee5W91+TycZr5nzu8vK6oNDPXOs06gOgyppMGu+r3A (using ssh-ed25519)
        Key ID: \"{rand_string}\"
        Serial: 0
        Valid: from 2023-11-05T01:35:00 to 2024-11-03T01:36:16
        Principals: 
                my-host.my-sld.my-tld
        Critical Options: (none)
        Extensions: (none)",
                "certificate_details_second_pass": "/etc/ssh/ssh_host_ed25519_key-cert.pub:
        Type: ssh-ed25519-cert-v01@openssh.com host certificate
        Public key: ED25519-CERT SHA256:p3hdvH7EBrRfA2yQPiaFnP29NFSxj+mtcjaTrjVNAs8
        Signing CA: ED25519 SHA256:jee5W91+TycZr5nzu8vK6oNDPXOs06gOgyppMGu+r3A (using ssh-ed25519)
        Key ID: \"{rand_string}\"
        Serial: 0
        Valid: from 2023-11-05T01:35:00 to 2024-11-03T01:36:16
        Principals: 
                my-host.my-sld.my-tld
        Critical Options: (none)
        Extensions: (none)",
                "configured_algorithm": "ed25519",
                "date_from": "2023-11-05",
                "date_to": "2024-11-03",
                "new_certificate_created": "false",
                "validity_duration_remaining": "364.0"
            },
            "installed": true
        }
    }
}
```

## Ansible AWX / Tower / Automation Platform


### Custom Credential Type

Host Certificate Authority Public and Signing Key.

``` json
{
    "name": "role/nfc_ssh/host_ca_signing_key",
    "description": "A Credential type for No Fuss Computings nfc_ssh role",
    "kind": "cloud",
    "inputs": {
        "fields": [
            {
                "id": "ca_public_key",
                "type": "string",
                "label": "Host Certificate Authority Public Key",
                "secret": false,
                "multiline": true
            },
            {
                "id": "ca_signing_key",
                "type": "string",
                "label": "Host Certificate Authority Signing Key",
                "secret": true,
                "multiline": true
            },
            {
                "id": "password",
                "type": "string",
                "label": "Key Decryption Password",
                "secret": true
            }
        ],
        "required": [
            "ca_public_key",
            "ca_signing_key"
        ]
    },
    "injectors": {
        "file": {
            "template": "{{ ca_signing_key }}"
        },
        "extra_vars": {
            "nfc_ssh_path_host_ca_key": "{{ tower.filename }}",
            "nfc_ssh_host_ca_public_key": "{{ ca_public_key }}",
            "nfc_ssh_host_ca_decryption_key": "{{ password | default('') }}"
        }
    }
}
```

User Certificate Authority Public Key.

``` json
{
    "name": "role/nfc_ssh/user_ca_public_key",
    "description": "A Credential type for No Fuss Computings nfc_ssh role",
    "kind": "cloud",
    "inputs": {
        "fields": [
            {
                "id": "ca_public_key",
                "type": "string",
                "label": "SSH User Certificate Authority Public Key",
                "secret": false,
                "multiline": true
            }
        ],
        "required": [
            "ca_public_key"
        ]
    },
    "injectors": {
        "extra_vars": {
            "nfc_ssh_user_ca_public_key": "{{ ca_public_key }}"
        }
    }
}
```
