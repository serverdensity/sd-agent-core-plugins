# Postfix Check

# Overview

This check monitors the size of all your Postfix queues.

# Installation

The Postfix check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=Postfix). To install the Postfix check install the `sd-agent-postfix` package.

# Configuration

Create a file `postfix.yaml` in the Agent's `conf.d` directory:

```
init_config:
  - postfix_user: postfix

instances:
  # add one instance for each postfix service you want to track
  - directory: /var/spool/postfix
    queues:
      - incoming
      - active
      - deferred
#   tags:
#     - optional_tag1
#     - optional_tag2
```

For each mail queue in `queues`, the Agent forks a `find` on its directory.
It uses `sudo` to do this with the privileges of the postfix user, so you must
add the following lines to `/etc/sudoers` for the Agent's user, `sd-agent`,
assuming postfix runs as `postfix`:
```
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/incoming -type f
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/active -type f
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/deferred -type f
```

Restart the Agent to start sending Postfix metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for postfix under the Checks section:

```
  Checks
  ======
    [...]

    postfix
    -------
      - instance #0 [OK]
      - Collected 3 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The postfix check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
