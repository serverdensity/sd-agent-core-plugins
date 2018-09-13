# Spark Check
## Overview

The Spark check collects metrics for:

- Drivers and executors: RDD blocks, memory used, disk used, duration, etc.
- RDDs: partition count, memory used, disk used
- Tasks: number of tasks active, skipped, failed, total
- Job state: number of jobs active, completed, skipped, failed

## Setup
### Installation

The Spark check is available from the sd-agent repository, so simply install `sd-agent-spark` on your:

- Mesos master (if you're running Spark on Mesos),
- YARN ResourceManager (if you're running Spark on YARN), or
- Spark master (if you're running Standalone Spark)


### Configuration

Create a file `spark.yaml` in the Agent's `conf.d` directory. See the [sample spark.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/spark/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - spark_url: http://localhost:8088 # Spark master web UI
#   spark_url: http://<Mesos_master>:5050 # Mesos master web UI
#   spark_url: http://<YARN_ResourceManager_address>:8088 # YARN ResourceManager address

    spark_cluster_mode: spark_standalone_mode # default is spark_yarn_mode
#   spark_cluster_mode: spark_mesos_mode
#   spark_cluster_mode: spark_yarn_mode

    cluster_name: <CLUSTER_NAME> # required; adds a tag 'cluster_name:<CLUSTER_NAME>' to all metrics

#   spark_pre_20_mode: true   # if you use Standalone Spark < v2.0
#   spark_proxy_enabled: true # if you have enabled the spark UI proxy
```

Set `spark_url` and `spark_cluster_mode` according to how you're running Spark.

Restart the Agent to start sending Spark metrics to Server Density.

### Validation

When you run `sd-agent info` you should see something like the following:

```
  Checks
  ======
    [...]

    spark
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The spark check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

