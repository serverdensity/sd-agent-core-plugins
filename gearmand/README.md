# Gearman Integration

## Overview

Collect Gearman metrics to:

* Visualize Gearman performance.
* Know how many tasks are queued or running.
* Correlate Gearman performance with the rest of your applications.

## Setup
### Installation

The Gearman check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=gearman). To install the gearman check install the `sd-agent-gearman` package.

### Configuration

Create a file `gearmand.yaml` in the Agent's `conf.d` directory. See the [sample gearmand.yaml](https://github.com/DataDog/integrations-core/blob/master/gearmand/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - server: localhost
    port: 4730
```

Restart the Agent to begin sending Gearman metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `gearmand` under the Checks section:

```
  Checks
  ======
    [...]

    gearmand
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The gearmand check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

