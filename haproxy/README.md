# Haproxy Integration

# Overview

Capture HAProxy activity in Server Density to:

* Visualize HAProxy load-balancing performance.
* Know when a server goes down.
* Correlate the performance of HAProxy with the rest of your applications.

# Installation

The HAProxy check can be installed with your package manager if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=haproxy). To install the haproxy check install the `sd-agent-haproxy` package.

# Configuration

## Prepare HAProxy

The Agent collects metrics via a stats endpoint. Configure one in your `haproxy.conf`:

```
listen stats :9000  # Listen on localhost:9000
mode http
stats enable  # Enable stats page
stats hide-version  # Hide HAProxy version
stats realm Haproxy\ Statistics  # Title text for popup window
stats uri /haproxy_stats  # Stats URI
stats auth <your_username>:<your_password>  # Authentication credentials
```

Restart HAProxy to enable the stats endpoint.

## Connect the Agent

Create a file `haproxy.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
    - url: https://localhost:9000/haproxy_stats
      username: <your_username>
      password: <your_password>
```

Restart the Agent to begin sending HAProxy metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `haproxy` under the Checks section:

```
  Checks
  ======
    [...]

    haproxy
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Troubleshooting

# Compatibility

The haproxy check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

