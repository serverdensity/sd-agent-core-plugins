# Gearman Integration

# Overview

Collect Gearman metrics to:

* Visualize Gearman performance.
* Know how many tasks are queued or running.
* Correlate Gearman performance with the rest of your applications.

# Installation

The Gearman check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=gearman). To install the gearman check install the `sd-agent-gearman` package.

# Configuration

Create a file `gearmand.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - server: localhost
    port: 4730
```

Restart the Agent to begin sending Gearman metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `gearmand` under the Checks section:

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

# Troubleshooting

# Compatibility

The gearmand check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

