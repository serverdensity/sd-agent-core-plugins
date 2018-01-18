# Agent Check: swap

## Overview

This check monitors the number of bytes a host has swapped in and swapped out.

## Setup
### Installation

The system swap check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=system+swap). To install the system swap check install the `sd-agent-system-swap` package.

### Configuration

Create a blank Agent check configuration file called `system_swap.yaml` in the Agent's `conf.d` directory. See the [sample system_swap.yaml](https://github.com/DataDog/integrations-core/blob/master/system_swap/conf.yaml.example) for all available configuration options:

```
# This check takes no initial configuration
init_config:

instances: [{}]
```

[Restart the Agent](https://docs.datadoghq.com/agent/faq/start-stop-restart-the-datadog-agent) to start collecting swap metrics.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `system_swap` under the Checks section:

```
  Checks
  ======
    [...]

    system_swap
    -------
      - instance #0 [OK]
      - Collected 2 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The system_swap check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
