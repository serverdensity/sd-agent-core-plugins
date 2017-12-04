# Cassandra Integration

# Overview

Get metrics from cassandra service in real time to:

* Visualize and monitor cassandra states
* Be notified about cassandra failovers and events.

# Installation

The Cassandra check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=cassandra). To install the cassandra check install the `sd-agent-cassandra` package.

# Configuration

# Validation

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

# Troubleshooting

# Compatibility

The cassandra check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

