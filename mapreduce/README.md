# Mapreduce Integration

## Overview

Get metrics from mapreduce service in real time to:

* Visualize and monitor mapreduce states
* Be notified about mapreduce failovers and events.

## Setup
### Installation

Install the `sd-agent-mapreduce` package manually or with your favorite configuration manager

### Configuration

Edit the `mapreduce.yaml` file to point to your server and port, set the masters to monitor. See the [sample mapreduce.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/mapreduce/conf.yaml.example) for all available configuration options.

### Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        mapreduce
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The mapreduce check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

