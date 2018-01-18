# PowerDNS Recursor Integration

## Overview

Track the performance of your PowerDNS recursors and monitor strange or worrisome traffic. This Agent check collects a wealth of metrics from your recursors, including those for:

* Query answer times — see how many responses take less than 1ms, 10ms, 100ms, 1s, and greater than 1s
* Query timeouts
* Cache hits and misses
* Answer rates by type — SRVFAIL, NXDOMAIN, NOERROR
* Ignored and dropped packets

And many more.

## Setup
### Installation

The PowerDNS check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=PowerDNS). To install the PowerDNS check install the `sd-agent-powerdns` package.

### Configuration
#### Prepare PowerDNS

This check collects performance statistics via pdns_recursor's statistics API. Versions of pdns_recursor before 4.1 do not enable the stats API by default. If you're running an older version, enable it by adding the following to your recursor config file (e.g. /etc/powerdns/recursor.conf):

```
webserver=yes
api-key=changeme            # only available since ver 4.0
webserver-readonly=yes      # default no
# webserver-port=8081       # default 8082
# webserver-address=0.0.0.0 # default 127.0.0.1
```

If you're running pdns_recursor 3.x, prepend `experimental-` to these option names, e.g. `experimental-webserver=yes`.

If you're running pdns_recursor >= 4.1, just set `api-key`.

Restart the recursor to enable the statistics API.

#### Connect the Agent

Create a file `powerdns_recursor.yaml` in the Agent's `conf.d` directory. See the [sample powerdns_recursor.yaml](https://github.com/DataDog/integrations-core/blob/master/powerdns_recursor/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - host: 127.0.0.1
    port: 8082
    api_key: changeme
    version: 4 # omit this line if you're running pdns_recursor version 3.x
```

Restart the Agent to begin sending PowerDNS Recursor metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `powerdns_recursor` under the Checks section:

```
  Checks
  ======
    [...]

    powerdns_recursor
    -------
      - instance #0 [OK]
      - Collected 8 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The PowerDNS Recursor check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

