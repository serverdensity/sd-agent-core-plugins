# Riak Check

## Overview

This check lets you track node, vnode and ring performance metrics from RiakKV or RiakTS.

## Setup
### Installation

The Riak check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=riak). To install the Riak check install the `sd-agent-riak` package.

### Configuration

Create a file `riak.yaml` in the Agent's `conf.d` directory. See the [sample riak.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/riak/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - url: http://127.0.0.1:8098/stats # or whatever your stats endpoint is
```

Restart the Agent to start sending Riak metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `riak` under the Checks section:

```
  Checks
  ======
    [...]

    riak
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The riak check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

