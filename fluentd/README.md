# Fluentd Integration

# Overview

Get metrics from Fluentd to:

* Visualize Fluentd performance.
* Correlate the performance of Fluentd with the rest of your applications.

# Installation

The Fluentd check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=fluentd). To install the fluentd check install the `sd-agent-fluentd` package.

# Configuration

## Prepare Fluentd

In your fluentd configuration, add a `monitor_agent` source:

```
<source>
  @type monitor_agent
  bind 0.0.0.0
  port 24220
</source>
```

## Connect the Server Density Agent

Create a file `fluentd.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - monitor_agent_url: http://localhost:24220/api/plugins.json
    #tag_by: "type" # defaults to 'plugin_id'
    #plugin_ids:    # collect metrics only on your chosen plugin_ids (optional)
    #  - plg1
    #  - plg2
```

Restart the Agent to begin sending Fluentd metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `fluentd` under the Checks section:

```
  Checks
  ======
    [...]

    fluentd
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

