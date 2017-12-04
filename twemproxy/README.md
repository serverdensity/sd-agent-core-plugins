# Twemproxy Integration

# Overview

Track overall and per-pool stats on each of your twemproxy servers. This Agent check collects metrics for client and server connections and errors, request and response rates, bytes in and out of the proxy, and more.

# Installation

The Twemproxy check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=Twemproxy). To install the Twemproxy check install the `sd-agent-twemproxy` package.

# Configuration

Create a file `twemproxy.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
    - host: localhost
      port: 2222 # change if your twemproxy doesn't use the default stats monitoring port
```

Restart the Agent to begin sending twemproxy metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `twemproxy` under the Checks section:

```
  Checks
  ======
    [...]

    twemproxy
    -------
      - instance #0 [OK]
      - Collected 20 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The twemproxy check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

