# Agent Check: Zookeeper

# Overview

The Zookeeper check tracks client connections and latencies, monitors the number of unprocessed requests, and more.

# Installation

The Zookeeper check is packaged with the Agent, so simply [install the Agent](https://support.serverdensity.com/hc/en-us/articles/214171178) on your Zookeeper servers. If you need the newest version of the check, install the `sd-agent-zk` package.

# Configuration

Create a file `zk.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - host: localhost
    port: 2181
    timeout: 3
```

Restart the Agent to start sending Zookeeper metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `zk` under the Checks section:

```
  Checks
  ======
    [...]

    zk
    -------
      - instance #0 [OK]
      - Collected 14 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The Zookeeper check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

