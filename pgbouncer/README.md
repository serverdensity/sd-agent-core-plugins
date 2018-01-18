# PgBouncer check

## Overview

The PgBouncer check tracks connection pool metrics and lets you monitor traffic to and from your application.

## Setup
### Installation

The PgBouncer check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=PgBouncer). To install the PgBouncer check install the `sd-agent-pgbouncer` package.

### Configuration

Create a file `pgbouncer.yaml` in the Agent's `conf.d` directory. See the [sample pgbouncer.yaml](https://github.com/DataDog/integrations-core/blob/master/pgbouncer/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - host: localhost
    port: 15433
    username: <YOUR_USERNAME>
    password: <YOUR_PASSWORD>
#   tags:
#     - env:prod
  - database_url: postgresql://<DB_USER>:<DB_PASS>@<DB_HOST>:<DB_PORT>/dbname?sslmode=require
#   tags:
#     - role:main
```

In your PGBouncer userlist.txt file add
```
  "datadog" "<your_pass>"
```

Next, in your PGBouncer pgbouncer.ini file add
```
stats_users = datadog
```

Restart the Agent to start sending PgBouncer metrics to Server Density.

### Validation

[Run the Agent's `info` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `pgbouncer` under the Checks section:

```
  Checks
  ======
    [...]

    pgbouncer
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The PgBouncer check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

