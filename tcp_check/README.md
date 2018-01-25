# Agent Check: TCP connectivity
{{< img src="integrations/tcpcheck/netgraphs.png" alt="Network Graphs" responsive="true" popup="true">}}
## Overview

Monitor TCP connectivity and response time for any host and port.

## Setup
### Installation

The TCP check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=tcp). To install the TCP check install the `sd-agent-tcp` package.


### Configuration

Create a file `tcp_check.yaml` in the Agent's `conf.d` directory. See the [sample tcp_check.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/tcp_check/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - name: SSH check
    host: jumphost.example.com # or an IPv4/IPv6 address
    port: 22
    skip_event: true # if false, the Agent will emit both events and service checks for this port; recommended true (i.e. only submit service checks)
    collect_response_time: true # to collect network.tcp.response_time. Default is false.
```

Configuration Options

* `name` (Required) - Name of the service. This will be included as a tag: `instance:<name>`. Note: This tag will have any spaces and dashes converted to underscores.
* `host` (Required) - Host to be checked. This will be included as a tag: `url:<host>:<port>`.
* `port` (Required) - Port to be checked. This will be included as a tag: `url:<host>:<port>`.
* `timeout` (Optional) - Timeout for the check. Defaults to 10 seconds.
* `collect_response_time` (Optional) - Defaults to false. If this is not set to true, no response time metric will be collected. If it is set to true, the metric returned is `network.tcp.response_time`.
* `skip_event` (Optional) - Defaults to false. Set to true to skip creating an event. This option will be removed in a future version and will default to true.
* `tags` (Optional) - Tags to be assigned to the metric.

Restart the Agent to start sending TCP service checks and response times to Server Density .

### Validation

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

## Compatibility

The TCP check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

