# Agent Check: TokuMX

## Overview

This check collects TokuMX metrics like:

* Opcounters
* Replication lag
* Cache table utilization and storage size

And more.

## Setup
### Installation

The TokuMX check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=tokumx). To install the TokuMX check install the `sd-agent-tokumx` package.

### Configuration
#### Prepare TokuMX

3.  Start the mongo shell.In it create a read-only user for the Server Density Agent in the `admin` database:

```
# Authenticate as the admin user.
use admin
db.auth("admin", "<YOUR_TOKUMX_ADMIN_PASSWORD>")
# Add a user for Server Density Agent
db.addUser("serverdensity", "<UNIQUEPASSWORD>", true)
```

4.  Verify that you created the user with the following command (not in the mongo shell).

        python -c 'from pymongo import Connection; print Connection().admin.authenticate("serverdensity", "<UNIQUEPASSWORD>")' | \
        grep True && \
        echo -e "\033[0;32mserverdensity user - OK\033[0m" || \
        echo -e "\033[0;31mserverdensity user - Missing\033[0m"

For more details about creating and managing users in MongoDB, refer to [the MongoDB documentation](http://www.mongodb.org/display/DOCS/Security+and+Authentication).

#### Connect the Agent

Create a file `tokumx.yaml` in the Agent's `conf.d` directory. See the [sample tokumx.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/tokumx/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - server: mongodb://serverdensity:<UNIQUEPASSWORD>@localhost:27017
```

Restart the Agent to start sending TokuMX metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `tokumx` under the Checks section:

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

## Compatibility

The tokumx check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

