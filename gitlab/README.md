# Gitlab Integration

## Overview

Integration that allows to:

* Visualize and monitor metrics collected via Gitlab through Prometheus

See https://docs.gitlab.com/ee/administration/monitoring/prometheus/ for
more information about Gitlab and its integration with Prometheus

## Setup
### Installation

Install the `sd-agent-gitlab` package manually or with your favorite configuration manager

### Configuration

Edit the `gitlab.yaml` file to point to the Gitlab's Prometheus metrics endpoint.
See the [sample gitlab.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/gitlab/conf.yaml.example) for all available configuration options.

The `allowed_metrics` item in the `init_config` section allows to specify the metrics that should be extracted.

### Validation

Run the Agent's `info` subcommand and look for `gitlab` under the Checks section:

    Checks
    ======

        gitlab
        -----------
          - instance #0 [OK]
          - Collected 8 metrics, 0 events & 3 service checks

## Compatibility

The gitlab check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).
