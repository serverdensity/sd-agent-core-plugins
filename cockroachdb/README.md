# Agent Check: CockroachDB

## Overview

The CockroachDB check monitors the overall health and performance of a [CockroachDB][1] cluster.

## Setup

### Installation

The cockroachdb check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=cockroachdb). To install the cockroachdb check install the `sd-agent-cockroachdb` package. To ensure the check runs, remove the `.example` extension from the configuration file (for packaged installs `/etc/sd-agent/conf.d/cockroachdb.yaml.example`), then restart sd-agent.

### Configuration

1. Edit the `cockroachdb.yaml` file, in the `conf.d/` folder to start collecting your cockroachdb performance data.
   See the [sample cockroachdb.d/conf.yaml][2] for all available configuration options.

2. Restart the Agent

### Validation

Run the Agent's `status` subcommand and look for `cockroachdb` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][3] for a list of metrics provided by this integration.

## Troubleshooting

Need help? [Contact Server Density Support](mailto:hello@serverdensity.com).

[1]: https://www.cockroachlabs.com/product/cockroachdb/
[2]: https://github.com/serverdensity/sd-agent-core-plugins/blob/master/cockroachdb/conf.yaml.example
[3]: https://github.com/serverdensity/sd-agent-core-plugins/blob/master/cockroachdb/metadata.csv

