# Btrfs Integration
{{< img src="integrations/btrfs/btrfs_metric.png" alt="btrfs metric" responsive="true" popup="true">}}
## Overview

Get metrics from btrfs service in real time to:

* Visualize and monitor btrfs states
* Be notified about btrfs failovers and events.

## Setup
### Installation

The btrfs check can be installed with your package manager, if the sd-agent is installed on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=btrfs). To install the btrfs check install the `sd-agent-btrfs` package.

### Configuration

1. Configure the Agent according to your needs, edit `conf.d/btrfs.yaml`. See the [sample btrfs.yaml](https://github.com/DataDog/integrations-core/blob/master/btrfs/conf.yaml.example) for all available configuration options.
2. [Restart the Agent](https://docs.datadoghq.com/agent/faq/start-stop-restart-the-datadog-agent)

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `btrfs` under the Checks section:

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
See [metadata.csv](https://github.com/DataDog/integrations-core/blob/master/btrfs/metadata.csv) for a list of metrics provided by this integration.

### Events
The Btrfs check does not include any event at this time.

### Service Checks
The Btrfs check does not include any service check at this time.

## Troubleshooting
Need help? Contact [Datadog Support](http://docs.datadoghq.com/help/).

