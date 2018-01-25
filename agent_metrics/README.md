# Agent_metrics Integration

## Overview

Get metrics from agent_metrics service in real time to:

* Visualize and monitor agent_metrics states
* Be notified about agent_metrics failovers and events.

## Setup
### Installation

Install the `sd-agent-agent-metrics` package manually or with your favorite configuration manager

### Configuration

Edit the `agent_metrics.yaml` file to point to your server and port, set the masters to monitor. See the [sample agent_metrics.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/agent_metrics/conf.yaml.default) for all available configuration options.

### Validation

When you run `sd-agent-agent info` you should see something like the following:

    Checks
    ======

        agent_metrics
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The Agent_metrics check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/agent_metrics/metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).
