# Network check
## Overview

The network check collects TCP/IP stats from the host operating system.

## Setup
### Installation

The network check is automatically installed with the Agent, so simply [install the Agent](https://support.serverdensity.com/hc/en-us/search?query=install) on any host. If you need the newest version of the check, install the `sd-agent-network` package.

### Configuration

The Agent enables the network check by default, but if you want to configure the check yourself, create a file `network.yaml` in the Agent's `conf.d` directory. See the [sample network.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/network/conf.yaml.default) for all available configuration options:

```
init_config:

instances:
  # Network check only supports one configured instance
  - collect_connection_state: false # set to true to collect TCP connection state metrics, e.g. SYN_SENT, ESTABLISHED
    excluded_interfaces: # the check will collect metrics on all other interfaces
      - lo
      - lo0
# ignore any network interface matching the given regex:
#   excluded_interface_re: eth1.*
```

Restart the Agent to effect any configuration changes.

### Validation

Run the Agent's `info` subcommand and look for `network` under the Checks section:

```
  Checks
  ======
    [...]

    network
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The network check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

