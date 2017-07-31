# Btrfs Integration

# Overview

Get metrics from btrfs service in real time to:

* Visualize and monitor btrfs states
* Be notified about btrfs failovers and events.

# Installation

The btrfs check can be installed with your package manager, if the sd-agent is installed on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=btrfs). To install the btrfs check install the `sd-agent-btrfs` package.

# Configuration

# Validation

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

# Troubleshooting

# Compatibility

The btrfs check is compatible with all major platforms.

# Metrics

