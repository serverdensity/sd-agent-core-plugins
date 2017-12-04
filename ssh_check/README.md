# Agent Check: SSH/SFTP

# Overview

This check lets you monitor SSH connectivity to remote hosts and SFTP response times.

# Installation

The SSH/SFTP check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=ssh+sftp). To install the SSH/SFTP check install the `sd-agent-ssh-check` package.

# Configuration

Create a file `ssh_check.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - host: <SOME_REMOTE_HOST>  # required
    username: <SOME_USERNAME> # required
    password: <SOME_PASSWORD> # or use private_key_file
#   private_key_file: <PATH_TO_PRIVATE_KEY>
#   private_key_type:         # rsa or ecdsa; default is rsa
#   port: 22                  # default is port 22
#   sftp_check: False         # set False to disable SFTP check; default is True
#   add_missing_keys: True    # default is False
```

Restart the Agent to start sending SSH/SFTP metrics and service checks to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `ssh_check` under the Checks section:

```
  Checks
  ======
    [...]

    ssh_check
    -------
      - instance #0 [OK]
      - Collected 1 metric, 0 events & 2 service check

    [...]
```

# Compatibility

The ssh check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

