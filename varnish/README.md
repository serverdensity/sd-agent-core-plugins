# Agent Check: Varnish
{{< img src="integrations/varnish/varnish.png" alt="Varnish default dashboard" responsive="true" popup="true">}}
## Overview

This check collects varnish metrics regarding:

* Clients: connections and requests
* Cache performance: hits, evictions, etc
* Threads: creation, failures, threads queued
* Backends: successful, failed, retried connections

It also submits service checks for the health of each backend.

## Setup
### Installation

Install the `sd-agent-varnish` package manually or with your favorite configuration manager

### Configuration

If you're running Varnish 4.1+, add the dd-agent system user to the varnish group (e.g. `sudo usermod -G varnish -a sd-agent`).

Then, create a file `varnish.yaml` in the Agent's `conf.d` directory. See the [sample varnish.yaml](https://github.com/DataDog/integrations-core/blob/master/varnish/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - varnishstat: /usr/bin/varnishstat        # or wherever varnishstat lives
    varnishadm: <PATH_TO_VARNISHADM_BIN>     # to submit service checks for the health of each backend
#   secretfile: <PATH_TO_VARNISH_SECRETFILE> # if you configured varnishadm and your secret file isn't /etc/varnish/secret
#   tags:
#     - instance:production
```

If you don't set `varnishadm`, the Agent won't check backend health. If you do set it, the Agent needs privileges to execute the binary with root privileges. Add the following to your `/etc/sudoers` file:

```
dd-agent ALL=(ALL) NOPASSWD:/usr/bin/varnishadm
```

[Restart the Agent](https://docs.datadoghq.com/agent/faq/start-stop-restart-the-datadog-agent) to start sending varnish metrics and service checks to Datadog.

### Validation

When you run `sd-agent info` you should see something like the following:

```
  Checks
  ======
    [...]

    varnish
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```
## Compatibility

The Varnish check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

