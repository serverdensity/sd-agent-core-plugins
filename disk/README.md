# Disk Check

## Overview

Collect metrics related to disk usage and IO.

## Setup
### Installation

The disk check is packaged with the Agent, so simply [install the Agent](https://support.serverdensity.com/hc/en-us/search?query=install) anywhere you wish to use it.

### Configuration

The disk check is enabled by default, and the Agent will collect metrics on all local partitions. If you want to configure the check with custom options, create a file `disk.yaml` in the Agent's `conf.d` directory. See the [sample disk.yaml](conf.yaml.default) for all available configuration options.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `disk` under the Checks section:

```
  Checks
  ======
    [...]

    disk
    -------
      - instance #0 [OK]
      - Collected 40 metrics, 0 events & 0 service checks

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
