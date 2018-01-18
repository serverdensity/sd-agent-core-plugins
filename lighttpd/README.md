# Lighttpd Check
{{< img src="integrations/lighttpd/lighttpddashboard.png" alt="Lighttpd Dashboard" responsive="true" popup="true">}}
## Overview

The Agent's lighttpd check tracks uptime, bytes served, requests per second, response codes, and more.

## Setup
### Installation

The Lighthttpd check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=lighthttpd). To install the lighthttpd check install the `sd-agent-lighthttpd` package.

You'll also need to install `mod_status` on your Lighttpd servers.

### Configuration

Create a file `lighttpd.yaml` in the Agent's `conf.d` directory. See the [sample lighttpd.yaml](https://github.com/DataDog/integrations-core/blob/master/lighttpd/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
# Each instance needs a lighttpd_status_url. Tags are optional.
  - lighttpd_status_url: http://example.com/server-status?auto
#   tags:
#     - instance:foo
```

Restart the Agent to begin sending lighttpd metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `lighttpd` under the Checks section:

```
  Checks
  ======
    [...]

    lighttpd
    -------
      - instance #0 [OK]
      - Collected 30 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The lighttpd check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

