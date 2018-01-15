# Agent Check: Storm

# Overview

The Storm check tracks topology statistics and latencies, as well as bolts and spouts.

# Installation

The Storm check is packaged with the Agent, so simply [install the Agent](https://support.serverdensity.com/hc/en-us/articles/214171178) on your Storm servers. If you need the newest version of the check, install the `sd-agent-storm` package.

# Configuration

Create a file `storm.yaml` in the Agent's `conf.d` directory and configure your Storm REST API host/port:

```
init_config:

instances:
  - server: 'http://localhost:8080'
```

Restart the Agent to start sending Storm metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `storm` under the Checks section:

```
  Checks
  ======
    [...]

    storm
    -----
      - instance #0 [OK]
      - Collected 76 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The Storm check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
