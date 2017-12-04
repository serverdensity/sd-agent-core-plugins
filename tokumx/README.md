# Agent Check: TokuMX

# Overview

This check collects TokuMX metrics like:

* Opcounters
* Replication lag
* Cache table utilization and storage size

And more.

# Installation

The TokuMX check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=apache). To install the TokuMX check install the `sd-agent-tokumx` package.

# Configuration

## Prepare TokuMX

In a Mongo shell, create a read-only user for the Server Density Agent in the `admin` database:

```
# Authenticate as the admin user.
use admin
db.auth("admin", "<YOUR_TOKUMX_ADMIN_PASSWORD>")
# Add a user for Server Density Agent
db.addUser("serverdensity", "<UNIQUEPASSWORD>", true)
```

## Connect the Agent

Create a file `tokumx.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - server: mongodb://serverdensity:<UNIQUEPASSWORD>@localhost:27017
```

Restart the Agent to start sending TokuMX metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `tokuxmx` under the Checks section:

```
  Checks
  ======
    [...]

    tokumx
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The tokumx check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
