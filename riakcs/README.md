# RiakCS Check

## Overview

Capture RiakCS metrics in Server Density to:

* Visualize key RiakCS metrics.
* Correlate RiakCS performance with the rest of your applications.

## Setup
### Installation

The RiakCS check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=RiakCS). To install the RiakCS check install the `sd-agent-riakcs` package.

### Configuration

Create a file `riakcs.yaml` in the Agent's `conf.d` directory. See the [sample riakcs.yaml](conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - host: localhost
    port: 8080
    access_id: <YOUR_ACCESS_KEY>
    access_secret: <YOUR_ACCESS_SECRET>
#   is_secure: true # set to false if your endpoint doesn't use SSL
#   s3_root: s3.amazonaws.com #
```

Restart the Agent to start sending RiakCS metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `riakcs` under the Checks section:

```
  Checks
  ======
    [...]

    riakcs
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The riakcs check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

