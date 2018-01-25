# Agent Check: Hadoop YARN
## Overview

This check collects metrics from your YARN ResourceManager, including:

* Cluster-wide metrics: number of running apps, running containers, unhealthy nodes, etc
* Per-application metrics: app progress, elapsed running time, running containers, memory use, etc
* Node metrics: available vCores, time of last health update, etc

And more.
## Setup
### Installation

The YARN check is packaged with the Agent, so simply [install the Agent](https://support.serverdensity.com/hc/en-us/articles/214171178) on your YARN ResourceManager. If you need the newest version of the check, install the `sd-agent-yarn` package.

### Configuration

Create a file `yarn.yaml` in the Agent's `conf.d` directory. See the [sample yarn.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/yarn/conf.yaml.example) for all available configuration options.:

```
init_config:

instances:
  - resourcemanager_uri: http://localhost:8088 # or whatever your resource manager listens
    cluster_name: MyCluster # used to tag metrics, i.e. 'cluster_name:MyCluster'; default is 'default_cluster'
    collect_app_metrics: true
```

See the [example check configuration](conf.yaml.example) for a comprehensive list and description of all check options.

Restart the Agent to start sending YARN metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `yarn` under the Checks section:

```
  Checks
  ======
    [...]

    yarn
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The yarn check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
