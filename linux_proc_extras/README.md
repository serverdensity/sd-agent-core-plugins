# Linux_proc_extras Integration

## Overview
Get metrics from linux_proc_extras service in real time to:

* Visualize and monitor linux_proc_extras states
* Be notified about linux_proc_extras failovers and events.

## Setup
### Installation

Install the `sd-agent-linux_proc_extras` package manually or with your favorite configuration manager

### Configuration

Edit the `linux_proc_extras.yaml` file to point to your server and port, set the masters to monitor. See the [sample linux_proc_extras.yaml](https://github.com/DataDog/integrations-core/blob/master/linux_proc_extras/conf.yaml.example) for all available configuration options.

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
The Linux proc extras check does not include any metric at this time.

