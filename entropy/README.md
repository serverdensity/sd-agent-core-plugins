# Entropy Check

## Overview

Collect the amount of available entropy on a linux system.

## Setup
### Installation

The entropy check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=entropy). To install the entropy check install the `sd-agent-entropy` package. To ensure the check runs, remove the `.example` extension from the configuration file (for packaged installs `/etc/sd-agent/conf.d/entropy.yaml.example`), then restart sd-agent.

### Configuration

The entropy check does not require any agent configuration. However, sudo is required for this check to function, meaning sudoers configuration may be required,

### Permissions
This check requires sudo to function. Here's an example for your sudoers file:

```
sd-agent ALL=(ALL) NOPASSWD: /bin/cat /proc/sys/kernel/random/entropy_avail
```

### Validation

Run the Agent's `info` subcommand and look for `entropy` under the Checks section:

```
  Checks
  ======
    [...]

    entropy
    -------
      - instance #0 [OK]
      - Collected 1 metrics, 0 events & 0 service checks

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
