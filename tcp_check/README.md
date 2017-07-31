# Agent Check: TCP connectivity

# Overview

Monitor TCP connectivity and response time for any host and port.

# Installation

The TCP check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=tcp). To install the TCP check install the `sd-agent-tcp` package.


# Configuration

Create a file `tcp_check.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - name: SSH check
    host: jumphost.example.com # or an IPv4/IPv6 address
    port: 22
    skip_event: true # if false, the Agent will emit both events and service checks for this port; recommended true (i.e. only submit service checks)
    collect_response_time: true # to collect network.tcp.response_time. Default is false.
```

Restart the Agent to start sending TCP service checks and response times to Server Density .

# Validation

Run the Agent's `info` subcommand and look for `tcp_check` under the Checks section:

```
  Checks
  ======
    [...]

    tcp_check
    ----------
      - instance #0 [OK]
      - Collected 1 metric, 0 events & 1 service check

    [...]
```

# Compatibility

The TCP check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

