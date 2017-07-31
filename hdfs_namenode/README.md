# HDFS NameNode Integration

# Overview

Monitor your primary _and_ standby HDFS NameNodes to know when your cluster falls into a precarious state: when you're down to one NameNode remaining, or when it's time to add more capacity to the cluster. This Agent check collects metrics for remaining capacity, corrupt/missing blocks, dead DataNodes, filesystem load, under-replicated blocks, total volume failures (across all DataNodes), and many more.

Use this check (hdfs_namenode) and its counterpart check (hdfs_datanode), not the older two-in-one check (hdfs); that check is deprecated.

# Installation

The HDFS NameNode check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=hdfs+namenode). To install the HDFS NameNode check install the `sd-agent-hdfs-namenode` package.

# Configuration

## Prepare the NameNode

The Agent collects metrics from the NameNode's JMX remote interface. The interface is disabled by default, so enable it by setting the following option in `hadoop-env.sh` (usually found in $HADOOP_HOME/conf):

```
export HADOOP_NAMENODE_OPTS="-Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  -Dcom.sun.management.jmxremote.port=50070 $HADOOP_NAMENODE_OPTS"
```

Restart the NameNode process to enable the JMX interface.

## Connect the Agent

Create a file `hdfs_namenode.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - hdfs_namenode_jmx_uri: http://localhost:50070
```

Restart the Agent to begin sending NameNode metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `hdfs_namenode` under the Checks section:

```
  Checks
  ======
    [...]

    hdfs_namenode
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Troubleshooting

# Compatibility

The hdfs_namenode check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

