# Gitlab Runner Integration

## Overview

Integration that allows to:

* Visualize and monitor metrics collected via Gitlab Runners through Prometheus
* Validate that the Gitlab Runner can connect to Gitlab

See https://docs.gitlab.com/runner/monitoring/README.html for
more information about Gitlab Runner and its integration with Prometheus

## Setup
### Installation

Install the `sd-agent-gitlab-runner` package manually or with your favorite configuration manager

### Configuration

Edit the `gitlab_runner.yaml` file to point to the Runner's Prometheus metrics endpoint and to the Gitlab master to have a service check.
See the [sample gitlab_runner.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/gitlab_runner/conf.yaml.example) for all available configuration options.

The `allowed_metrics` item in the `init_config` section allows to specify the metrics that should be extracted.

**Remarks:**

 - Some metrics should be reported as `rate` (i.e., `ci_runner_errors`)


### Validation

Run the Agent's `info` subcommand and look for `gitlab_runner` under the Checks section:

    Checks
    ======

        gitlab_runner
        -----------
          - instance #0 [OK]
          - Collected 10 metrics, 0 events & 2 service checks

## Compatibility

The gitlab_runner check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.


## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).

