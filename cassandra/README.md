# Cassandra Integration
## Overview

Get metrics from cassandra service in real time to:

* Visualize and monitor cassandra states
* Be notified about cassandra failovers and events.

## Setup
### Installation

The Cassandra check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=cassandra). To install the cassandra check install the `sd-agent-cassandra` package.

We recommend the use of Oracle's JDK for this integration.

This check has a limit of 350 metrics per instance. The number of returned metrics is indicated in the info page. You can specify the metrics you are interested in by editing the configuration below.

### Configuration

1. Configure the Agent to connect to Cassandra, just edit `conf.d/cassandra.yaml`. See the [sample  cassandra.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/cassandra/conf.yaml.example) for all available configuration options.
2. Restart the Agent

### Validation

Run the Agent's `info` subcommand and look for `cassandra` under the Checks section:

```
  Checks
  ======
    [...]

    cassandra
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The cassandra check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

