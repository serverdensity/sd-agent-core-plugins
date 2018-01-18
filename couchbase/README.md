# Couchbase Integration
{{< img src="integrations/couchbase/couchbase_graph.png" alt="couchbase graph" responsive="true" popup="true">}}
## Overview

Identify busy buckets, track cache miss ratios, and more. This Agent check collects metrics like:

* Hard disk and memory used by data
* Current connections
* Total objects
* Operations per second
* Disk write queue size

And many more.

## Setup
### Installation

The Couchbase check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=cpuchbase). To install the couchbase check install the `sd-agent-couchbase` package.

### Configuration

Create a file `couchbase.yaml` in the Agent's `conf.d` directory. See the [sample couchbase.yaml](https://github.com/DataDog/integrations-core/blob/master/couchbase/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - server: http://localhost:8091 # or wherever your Couchbase is listening
    #user: <your_username>
    #password: <your_password>
```

Restart the Agent to begin sending Couchbase metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `couchbase` under the Checks section:

```
  Checks
  ======
    [...]

    couchbase
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The couchbase check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

