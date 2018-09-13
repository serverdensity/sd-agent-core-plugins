# Agent Check: Kafka Consumer

## Overview

This Agent check only collects metrics for message offsets. If you want to collect metrics about the Kafka brokers themselves, see the kafka check.

This check fetches the highwater offsets from the Kafka brokers, consumer offsets for old-style consumers that store their offsets in zookeeper, and the calculated consumer lag (which is the difference between those two metrics).

This check does NOT support Kafka versions > 0.8—it can't collect consumer offsets for new-style consumer groups which store their offsets in Kafka.

## Setup
### Installation

Install the `sd-agent-kafka-consumer` package manually or with your favorite configuration manager

### Configuration

Create a `kafka_consumer.yaml` file using [this sample conf file](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/kafka_consumer/conf.yaml.example) as an example. Then restart the sd-agent to start sending metrics to Server Density.

### Validation

When you run `info` subcommand you should see something like the following:

```
  Checks
  ======
    [...]

    kafka_consumer
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The kafka_consumer check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.


## Troubleshooting
### Specifying a non existent partition in your kafka_Consumer.yaml file
If you get this error in your info.log:
```
instance - #0 [Error]: ''
```

Specify the specific partition of your environment for your topic in your kafka_Consumer.yaml file:
```
#my_topic [0, 1, 4, 12]
```
