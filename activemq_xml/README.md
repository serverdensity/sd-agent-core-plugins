# Activemq_xml Integration

## Overview

Get metrics from activemq_xml service in real time to:

* Visualize and monitor activemq_xml states
* Be notified about activemq_xml failovers and events.

## Setup
### Installation

Install the `sd-agent-activemq-xml` package manually or with your favorite configuration manager

### Configuration

Edit the `activemq_xml.yaml` file to point to your server and port, set the masters to monitor. See the [sample activemq_xml.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/activemq_xml/conf.yaml.example) for all available configuration options.

### Validation

When you run `sd-agent-agent info` you should see something like the following:

    Checks
    ======

        activemq_xml
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The activemq_xml check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/activemq_xml/metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).

