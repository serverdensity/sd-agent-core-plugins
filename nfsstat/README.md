# Nfsstat Integration

## Overview

nfsiostat is a tool that gets metrics from NFS mounts. This check grabs these metrics.

## Setup
### Installation

Install the `sd-agent-nfsstat` package manually or with your favorite configuration manager

### Configuration

Edit the `nfsstat.yaml` file to point to your nfsiostat binary script, or use the one included with the binary installer. See the [sample nfsstat.yaml](https://github.com/serverdensity/sd-agent/blob/master/nfsstat/conf.yaml.example) for all available configuration options.

### Validation

Run the Agent's `info` subcommand and look for `nfsstat` under the Checks section:

    Checks
    ======

        nfsstat
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The nfsstat check is compatible with linux

## Data Collected
### Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/nfsstat/metadata.csv) for a list of metrics provided by this check.


## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).

