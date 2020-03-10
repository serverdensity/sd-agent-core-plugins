# Mdadm Check

## Overview

Collect the metrics from madam devices and disks.

## Setup
### Installation

The mdadm check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=mdadm). To install the mdadm check install the `sd-agent-mdadm` package. To ensure the check runs, remove the `.example` extension from the configuration file (for packaged installs `/etc/sd-agent/conf.d/mdadm.yaml.example`), then restart sd-agent.

### Configuration

The mdadm check does not require any agent configuration.

### Validation

Run the Agent's `info` subcommand and look for `mdadm` under the Checks section:

```
  Checks
  ======
    [...]

    mdadm
    -------
      - instance #0 [OK]
      - Collected 1 metrics, 0 events & 0 service checks

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
