# Haproxy Integration
{{< img src="integrations/haproxy/haproxydash.png" alt="HAProxy default dashboard" responsive="true" popup="true">}}
## Overview

Capture HAProxy activity in Server Density to:

* Visualize HAProxy load-balancing performance.
* Know when a server goes down.
* Correlate the performance of HAProxy with the rest of your applications.

## Setup
### Installation

The HAProxy check can be installed with your package manager if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=haproxy). To install the haproxy check install the `sd-agent-haproxy` package.

Make sure that stats are enabled on your HAProxy configuration. See [this post for guidance on doing this](https://www.datadoghq.com/blog/how-to-collect-haproxy-metrics/).

### Configuration
#### Prepare HAProxy

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

### Connect the Agent

Create a file `haproxy.yaml` in the Agent's `conf.d` directory. See the [sample haproxy.yaml](https://github.com/DataDog/integrations-core/blob/master/haproxy/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
    - url: https://localhost:9000/haproxy_stats
      username: <your_username>
      password: <your_password>
```

Restart the Agent to begin sending HAProxy metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `haproxy` under the Checks section:

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

## Compatibility
The haproxy check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

