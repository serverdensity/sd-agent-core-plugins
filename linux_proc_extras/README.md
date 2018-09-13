# Linux_proc_extras Integration

## Overview
Get metrics from linux_proc_extras service in real time to:

* Visualize and monitor linux_proc_extras states
* Be notified about linux_proc_extras failovers and events.

## Setup
### Installation

Install the `sd-agent-linux-proc-extras` package manually or with your favorite configuration manager

### Configuration

Ensure the `linux_proc_extras.yaml` file is present in the agent config directory. No configuration is required for this check.

### Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        linux_proc_extras
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The linux_proc_extras check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/linux_proc_extra/metadata.csv) for a list of metrics provided by this integration.

