# Agent Check: StatsD

## Overview

This check monitors the availability and uptime of non-Server Density StatsD servers. It also tracks the number of metrics, by metric type, received by StatsD.

This check does **NOT** forward application metrics from StatsD servers to Server Density. It collects metrics about StatsD itself.

## Setup
### Installation

Install the `sd-agent-statsd` package manually or with your favorite configuration manager

### Configuration

Create a file `statsd.yaml` in the Agent's `conf.d` directory. See the [sample statsd.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/statsd/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - host: localhost
    port: 8126 # or wherever your statsd listens
```

Restart the Agent to start sending StatsD metrics and service checks to Server Density.

### Validation

When you run `sd-agent info` you should see something like the following:

```
  Checks
  ======
    [...]

    statsd
    -------
      - instance #0 [OK]
      - Collected 3 metrics, 0 events & 2 service checks

    [...]
```

## Compatibility

The statsd check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

