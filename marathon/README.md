# Marathon Integration

## Overview

The Agent's Marathon check lets you:

* Track the state and health of every application: see configured memory, disk, cpu, and instances; monitor the number of healthy and unhealthy tasks
* Monitor the number of queued applications and the number of deployments

## Setup
### Installation

The Marathon check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=marathon). To install the marathon check install the `sd-agent-marathon` package.

### Configuration

Create a file `marathon.yaml` in the Agent's `conf.d` directory. See the [sample marathon.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/marathon/conf.yaml.example) for all available configuration options:

```
init_config:
  - default_timeout: 5 # how many seconds to wait for Marathon API response

instances:
  - url: https://<server>:<port> # the API endpoint of your Marathon master; required
#   acs_url: https://<server>:<port> # if your Marathon master requires ACS auth
    user: <username> # the user for marathon API or ACS token authentication
    password: <password> # the password for marathon API or ACS token authentication
```

The function of `user` and `password` depends on whether or not you configure `acs_url`; If you do, the Agent uses them to request an authentication token from ACS, which it then uses to authenticate to the Marathon API. Otherwise, the Agent uses `user` and `password` to directly authenticate to the Marathon API.

Restart the Agent to begin sending Marathon metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `marathon` under the Checks section:

```
  Checks
  ======
    [...]

    marathon
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The marathon check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

