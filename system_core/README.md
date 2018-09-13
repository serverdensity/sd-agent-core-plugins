# Agent Check: system cores
## Overview

This check collects the number of CPU cores on a host and CPU times (i.e. system, user, idle, etc).

## Setup
### Installation

The system_core check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=system_core). To install the system_core check install the `sd-agent-system-core` package.

### Configuration

Create a file `system_core.yaml` in the Agent's `conf.d` directory. See the [sample system_core.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/system_core/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - foo: bar
```

The Agent just needs one item in `instances` in order to enable the check. The content of the item doesn't matter.

Restart the Agent to enable the check.

### Validation

Run the Agent's `info` subcommand and look for `system_core` under the Checks section:

```
  Checks
  ======
    [...]

    system_core
    -------
      - instance #0 [OK]
      - Collected 5 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The system_core check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

Depending on the platform, the check may collect other CPU time metrics, e.g. `system.core.interrupt` on Windows, `system.core.iowait` on Linux, etc.


## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).
