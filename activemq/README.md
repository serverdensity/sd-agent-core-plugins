# Activemq Integration

## Overview

The ActiveMQ check lets you collect metrics for brokers and queues, producers and consumers, and more.

## Setup
### Installation

Install the `sd-agent-activemq` package manually or with your favorite configuration manager

### Configuration

1. **Make sure that [JMX Remote is enabled](http://activemq.apache.org/jmx.html) on your ActiveMQ server.**
2. Configure the agent to connect to ActiveMQ. Edit `${confd_help('`conf.d/activemq.yaml`')}`. See the [sample activemq.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/activemq/conf.yaml.example) for all available configuration options.

```
instances:
  - host: localhost
    port: 7199
    user: username
    password: password
    name: activemq_instance
# List of metrics to be collected by the integration
# You should not have to modify this.
init_config:
  conf:
    - include:
      Type: Queue
      attribute:
        AverageEnqueueTime:
          alias: activemq.queue.avg_enqueue_time
          metric_type: gauge
        ConsumerCount:
          alias: activemq.queue.consumer_count
          metric_type: gauge
        ProducerCount:
          alias: activemq.queue.producer_count
          metric_type: gauge
        MaxEnqueueTime:
          alias: activemq.queue.max_enqueue_time
          metric_type: gauge
        MinEnqueueTime:
          alias: activemq.queue.min_enqueue_time
          metric_type: gauge
        MemoryPercentUsage:
          alias: activemq.queue.memory_pct
          metric_type: gauge
        QueueSize:
          alias: activemq.queue.size
          metric_type: gauge
        DequeueCount:
          alias: activemq.queue.dequeue_count
          metric_type: counter
        DispatchCount:
          alias: activemq.queue.dispatch_count
          metric_type: counter
        EnqueueCount:
          alias: activemq.queue.enqueue_count
          metric_type: counter
        ExpiredCount:
          alias: activemq.queue.expired_count
          type: counter
        InFlightCount:
          alias: activemq.queue.in_flight_count
          metric_type: counter

    - include:
      Type: Broker
      attribute:
        StorePercentUsage:
          alias: activemq.broker.store_pct
          metric_type: gauge
        TempPercentUsage:
          alias: activemq.broker.temp_pct
          metric_type: gauge
        MemoryPercentUsage:
          alias: activemq.broker.memory_pct
          metric_type: gauge
```

3. Restart the agent

```bash
sudo /etc/init.d/sd-agent restart
```
or
```bash
sudo systemctl restart sd-agent
```
### Validation

Run the Agent's `info` subcommand and look for `activemq` under the Checks section:

```bash
sudo /usr/share/python/sd-agent/agent.py info
```

```
  Checks
  ======
    [...]

    activemq
    -------
      - instance #0 [OK]
      - Collected 8 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The ActiveMQ check only runs on Linux or Mac (OS X or macOS).

## Metrics
See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/activemq/metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).
