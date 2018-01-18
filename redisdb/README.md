# Redis Integration

## Overview

Whether you use Redis as a database, cache, or message queue, this integration helps you track problems with your Redis servers and the parts of your infrastructure that they serve. The Server Density Agent's Redis check collects a wealth of metrics related to performance, memory usage, blocked clients, slave connections, disk persistence, expired and evicted keys, and many more.

## Setup
### Installation

The Redis check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=redis). To install the Redis check install the `sd-agent-redis` package.

### Configuration

Create a `redisdb.yaml` in the Server Density Agent's `conf.d` directory:

```
init_config:

instances:
  - host: localhost
    port: 6379 # or wherever your redis listens
#   unix_socket_path: /var/run/redis/redis.sock # if your redis uses a socket instead of TCP
#   password: myredispassword                   # if your redis requires auth
```

Configuration Options:

* `unix_socket_path` - (Optional) - Can be used instead of `host` and `port`.
* `db`, `password`, and `socket_timeout` - (Optional) - Additional connection options.
* `warn_on_missing_keys` - (Optional) - Display a warning in the info page if the keys we're tracking are missing.
* `slowlog-max-len` - (Optional) - Maximum number of entries to fetch from the slow query log. By default, the check will
        read this value from the redis config. If it's above 128, it will default to 128 due to potential increased latency
        to retrieve more than 128 slowlog entries every 15 seconds. If you need to get more entries from the slow query logs
        set the value here. Warning: It may impact the performance of your redis instance
* `command_stats` - (Optional) - Collect INFO COMMANDSTATS output as metrics.

See [this sample redisdb.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/redisdb/conf.yaml.example) for all available configuration options.

Restart the Agent to begin sending Redis metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `redisdb` under the Checks section:

```
  Checks
  ======
    [...]

    redisdb
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The redis check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting

* [Redis Integration Error: "unknown command 'CONFIG'"](https://docs.datadoghq.com/integrations/faq/redis-integration-error-unknown-command-config)

### Agent cannot connect
```
    redisdb
    -------
      - instance #0 [ERROR]: 'Error 111 connecting to localhost:6379. Connection refused.'
      - Collected 0 metrics, 0 events & 1 service chec
```

Check that the connection info in `redisdb.yaml` is correct.

### Agent cannot authenticate
```
    redisdb
    -------
      - instance #0 [ERROR]: 'NOAUTH Authentication required.'
      - Collected 0 metrics, 0 events & 1 service check
```

Configure a `password` in `redisdb.yaml`.

