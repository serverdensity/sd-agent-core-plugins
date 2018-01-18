# DNS Integration

## Overview

Monitor the resolvability of and lookup times for any DNS records using nameservers of your choosing.

## Setup
### Installation

The DNS check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=dns). To install the dns check install the `sd-agent-dns` package.

Though many metrics-oriented checks are best run on the same host(s) as the monitored service, you may want to run this status-oriented check from hosts that do not run the monitored DNS services.

### Configuration

Create a file `dns_check.yaml` in the Agent's `conf.d` directory. See the [sample dns_check.yaml](https://github.com/DataDog/integrations-core/blob/master/dns_check/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - name: Example (com)
    # nameserver: 8.8.8.8   # The nameserver to query, this must be an IP address
    hostname: example.com # the record to fetch
    # record_type: AAAA   # default is A
  - name: Example (org)
    hostname: example.org
```

If you omit the `nameserver` option, the check will use whichever nameserver is configured in local network settings.

Restart the Agent to begin sending DNS service checks and response times to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `dns_check` under the Checks section:

```
  Checks
  ======
    [...]

    dns_check
    ---------
      - instance #0 [OK]
      - instance #1 [OK]
      - Collected 2 metrics, 0 events & 2 service checks

    [...]
```

## Compatibility

The DNS check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
