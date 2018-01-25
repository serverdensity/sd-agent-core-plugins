# Btrfs Integration
## Overview

Get metrics from btrfs service in real time to:

* Visualize and monitor btrfs states
* Be notified about btrfs failovers and events.

## Setup
### Installation

The btrfs check can be installed with your package manager, if the sd-agent is installed on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=btrfs). To install the btrfs check install the `sd-agent-btrfs` package.

### Configuration

1. Configure the Agent according to your needs, edit `conf.d/btrfs.yaml`. See the [sample btrfs.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/btrfs/conf.yaml.example) for all available configuration options.
2. Restart the Agent

### Validation

Run the Agent's `info` subcommand and look for `btrfs` under the Checks section:

```
  Checks
  ======
    [...]

    btrfs
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The Btrfs check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/btrfs/metadata.csv) for a list of metrics provided by this integration.


## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).

