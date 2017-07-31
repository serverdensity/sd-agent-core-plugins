# Lighttpd Check

# Overview

The Agent's lighttpd check tracks uptime, bytes served, requests per second, response codes, and more.

# Installation

The Lighthttpd check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=lighthttpd). To install the lighthttpd check install the `sd-agent-lighthttpd` package.

You'll also need to install `mod_status` on your Lighttpd servers.

# Configuration

Create a file `lighttpd.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
# Each instance needs a lighttpd_status_url. Tags are optional.
  - lighttpd_status_url: http://example.com/server-status?auto
#   tags:
#     - instance:foo
```

Restart the Agent to begin sending lighttpd metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `lighttpd` under the Checks section:

```
  Checks
  ======
    [...]

    lighttpd
    -------
      - instance #0 [OK]
      - Collected 30 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The lighttpd check is compatible with all major platforms.

# Metrics

The check collects different metrics depending on the major version of lighttpd.

It collects these metrics for lighttpd 1:

- lighttpd.net.bytes
- lighttpd.net.bytes_per_s
- lighttpd.net.hits
- lighttpd.net.request_per_s
- lighttpd.performance.busy_servers
- lighttpd.performance.idle_server
- lighttpd.performance.uptime

It collects these metrics for lighttpd 2:

- lighttpd.connections.state_handle_request
- lighttpd.connections.state_keep_alive
- lighttpd.connections.state_read_header
- lighttpd.connections.state_start
- lighttpd.connections.state_write_response
- lighttpd.net.bytes_in
- lighttpd.net.bytes_in_avg
- lighttpd.net.bytes_in_avg_5sec
- lighttpd.net.bytes_out
- lighttpd.net.bytes_out_avg
- lighttpd.net.bytes_out_avg_5sec
- lighttpd.net.connections_avg
- lighttpd.net.connections_avg_5sec
- lighttpd.net.connections_total
- lighttpd.net.requests_avg
- lighttpd.net.requests_avg_5sec
- lighttpd.net.requests_total
- lighttpd.performance.memory_usage
- lighttpd.performance.uptime
- lighttpd.response.status_1xx
- lighttpd.response.status_2xx
- lighttpd.response.status_3xx
- lighttpd.response.status_4xx
- lighttpd.response.status_5xx

See [metadata.csv](metadata.csv) for a description of metrics provided by this check.

