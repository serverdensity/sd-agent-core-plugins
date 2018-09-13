# Agent Check: Kafka

## Overview

Connect Kafka to Server Density in order to:

* Visualize the performance of your cluster in real time
* Correlate the performance of Kafka with the rest of your applications

This check has a limit of 350 metrics per instance. The number of returned metrics is indicated in the info page. You can specify the metrics you are interested in by editing the configuration below.

Install the `sd-agent-kafka` package manually or with your favorite configuration manager


## Setup
### Installation

Ensure that you have the sd-agent repostiory configured and install the `sd-agent-kafka` package.

The check collects metrics via JMX, so you'll need a JVM on each kafka node so the Agent can connect. You can use the same JVM that Kafka uses.

### Configuration

Configure a `kafka.yaml` in the sd-agent's `conf.d` directory. Kafka bean names depend on the exact Kafka version you're running. You should always use the example that comes packaged with the Agent as a base since that will be the most up-to-date configuration. Use [this sample conf file](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/kafka/conf.yaml.example) as an example.

After you've configured `kafka.yaml`, restart the Agent to begin sending Kafka metrics to Server Density.

### Validation

When you run `sd-agent info` you should see something like the following:

```
  Checks
  ======
    [...]

    kafka-localhost-9999
    -------
      - instance #0 [OK]
      - Collected 8 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The kafka check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

