# RabbitMQ Check
## Overview

The RabbitMQ check lets you:

* Track queue-based stats: queue size, consumer count, unacknowledged messages, redelivered messages, etc
* Track node-based stats: waiting processes, used sockets, used file descriptors, etc
* Monitor vhosts for aliveness and number of connections

And more.
## Setup
### Installation

The rabbitmq check can be installed with your package manager, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=rabbitmq).

### Configuration
#### Prepare RabbitMQ

You must enable the RabbitMQ management plugin. See [RabbitMQ's documentation](https://www.rabbitmq.com/management.html) to enable it.

#### Connect the Agent

Create a file `rabbitmq.yaml` in the Agent's `conf.d` directory. See the [sample rabbitmq.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/rabbitmq/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
- rabbitmq_api_url: http://localhost:15672/api/
#   rabbitmq_user: <RABBIT_USER> # if your rabbitmq API requires auth; default is guest
#   rabbitmq_pass: <RABBIT_PASS> # default is guest
#   tag_families: true           # default is false
#   vhosts:
#     - <THE_ONE_VHOST_YOU_CARE_ABOUT>
```

If you don't set `vhosts`, the Agent sends the following for EVERY vhost:

1. the `rabbitmq.aliveness` service check
1. the `rabbitmq.connections` metric

If you do set `vhosts`, the Agent sends this check and metric only for the vhosts you list.

There are options for `queues` and `nodes` that work similarly—the Agent checks all queues and nodes by default, but you can provide lists or regexes to limit this. See the [example check configuration](conf.yaml.example) for details on these configuration options (and all others).

Configuration Options

* `rabbitmq_api_url` - **required** - Points to the api url of the [RabbitMQ Managment Plugin](http://www.rabbitmq.com/management.html)
* `rabbitmq_user` - **optional** - Defaults to 'guest'
* `rabbitmq_pass` - **optional** - Defaults to 'guest'
* `tag_families` - **optional** - Defaults to false - Tag queue "families" based off of regex matching
* `nodes` or `nodes_regexes` - **optional** - Use the `nodes` or `nodes_regexes` parameters to specify the nodes you'd like to collect metrics on (up to 100 nodes). If you have less than 100 nodes, you don't have to set this parameter, the metrics will be collected on all the nodes by default. See the link to the example YAML below for more.
* `queues` or `queues_regexes` - **optional** - Use the `queues` or `queues_regexes` parameters to specify the queues you'd like to collect metrics on (up to 200 queues). If you have less than 200 queues, you don't have to set this parameter, the metrics will be collected on all the queues by. default. If you have set up vhosts, set the queue names as `vhost_name/queue_name`. If you have `tag_families` enabled, the first captured group in the regex will be used as the queue_family tag.  See the link to the example YAML below for more.
* `vhosts` - **optional** - By default a list of all vhosts is fetched and each one will be checked using the aliveness API. If you prefer only certain vhosts to be monitored with service checks then you can list the vhosts you care about.

Restart the Agent to begin sending RabbitMQ metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `rabbitmq` under the Checks section:

```
  Checks
  ======
    [...]

    rabbitmq
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 2 service checks

    [...]
```

## Compatibility

The rabbitmq check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

The Agent tags `rabbitmq.queue.*` metrics by queue name, and `rabbitmq.node.*` metrics by node name.

