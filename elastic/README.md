# Elasticsearch Integration
{{< img src="integrations/elasticsearch/elasticsearchgraph.png" alt="Elasticsearch" responsive="true" popup="true">}}

## Overview

Stay up-to-date on the health of your Elasticsearch cluster, from its overall status down to JVM heap usage and everything in between. Get notified when you need to revive a replica, add capacity to the cluster, or otherwise tweak its configuration. After doing so, track how your cluster metrics respond.

The Server Density Agent's Elasticsearch check collects metrics for search and indexing performance, memory usage and garbage collection, node availability, shard statistics, disk space and performance, pending tasks, and many more. The Agent also sends events and service checks for the overall status of your cluster.

## Setup
### Installation

The Elasticsearch check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=elasticsearch). To install the elasticsearch check install the `sd-agent-elastic` package on your Elasticserch hosts, or on some other server if you use a hosted Elasticsearch (e.g. Elastic Cloud).

### Configuration

1. Create a file `elastic.yaml` in the Server Density Agent's `conf.d` directory:

```
init_config:

instances:
  - url: http://localhost:9200 # or wherever your cluster API is listening
    cluster_stats: false # set true ONLY if you're not running the check on each cluster node
    pshard_stats: true
    pending_task_stats: true
```

If you're collecting Elasticsearch metrics from just one Server Density Agent running outside the cluster — e.g. if you use a hosted Elasticsearch — set `cluster_stats` to true.

See the [sample elastic.yaml](conf.yaml.example) for all available configuration options, including those for authentication to and SSL verification of your cluster's API `url`.

2. Restart the Agent to begin sending Elasticsearch metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `elastic` under the Checks section:

```
  Checks
  ======
    [...]

    elastic
    -------
      - instance #0 [OK]
      - Collected 118 metrics, 0 events & 2 service checks

    [...]
```

## Compatibility

The Elasticsearch check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

