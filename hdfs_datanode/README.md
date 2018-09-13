# HDFS DataNode Integration

## Overview

Track disk utilization and failed volumes on each of your HDFS DataNodes. This Agent check collects metrics for these, as well as block- and cache-related metrics.

Use this check (hdfs_datanode) and its counterpart check (hdfs_namenode), not the older two-in-one check (hdfs); that check is deprecated.

## Setup
### Installation

The HDFS Datanode check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=hdfs+datanode). To install the HDFS Datanode check install the `sd-agent-hdfs-datanode` package.

### Configuration
#### Prepare the DataNode

The Agent collects metrics from the DataNode's JMX remote interface. The interface is disabled by default, so enable it by setting the following option in `hadoop-env.sh` (usually found in $HADOOP_HOME/conf):

```
export HADOOP_DATANODE_OPTS="-Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  -Dcom.sun.management.jmxremote.port=50075 $HADOOP_DATANODE_OPTS"
```

Restart the DataNode process to enable the JMX interface.

#### Connect the Agent

Create a file `hdfs_datanode.yaml` in the Agent's `conf.d` directory. See the [sample hdfs_datanode.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/hdfs_datanode/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - hdfs_datanode_jmx_uri: http://localhost:50075
```

Restart the Agent to begin sending DataNode metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `hdfs_datanode` under the Checks section:

```
  Checks
  ======
    [...]

    hdfs_datanode
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The hdfs_datanode check is compatible with all major platforms.


## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

