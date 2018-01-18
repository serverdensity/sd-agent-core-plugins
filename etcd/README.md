# Etcd Integration
{{< img src="integrations/etcd/etcd_graph.png" alt="Etcd Graph" responsive="true" popup="true">}}
## Overview

Collect etcd metrics to:

* Monitor the health of your etcd cluster.
* Know when host configurations may be out of sync.
* Correlate the performance of etcd with the rest of your applications.

## Setup
### Installation

The etcd check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=etcd). To install the etcd check install the `sd-agent-etcd` package.

### Configuration

Create a file `etcd.yaml` in the Agent's `conf.d` directory. See the [sample etcd.yaml](https://github.com/DataDog/integrations-core/blob/master/etcd/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - url: "https://server:port" # API endpoint of your etcd instance
```

Restart the Agent to begin sending etcd metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `etcd` under the Checks section:

```
  Checks
  ======
    [...]

    etcd
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The etcd check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

etcd metrics are tagged with `etcd_state:leader` or `etcd_state:follower`, depending on the node status, so you can easily aggregate metrics by status.

