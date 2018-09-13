# Agent Check: Apache Web Server
## Overview

The Apache check tracks requests per second, bytes served, number of worker threads, service uptime, and more.

## Setup
### Installation

The Apache check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=apache). To install the apache check install the `sd-agent-apache` package.

Install `mod_status` on your Apache servers and enable `ExtendedStatus`.

### Configuration

Create a file `apache.yaml` in the Agent's `conf.d` directory. See the [sample apache.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/apache/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - apache_status_url: http://example.com/server-status?auto
#   apache_user: example_user # if apache_status_url needs HTTP basic auth
#   apache_password: example_password
#   disable_ssl_validation: true # if you need to disable SSL cert validation, i.e. for self-signed certs
```

Restart the Agent to start sending Apache metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `apache` under the Checks section:

```
  Checks
  ======
    [...]

    apache
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The Apache check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

