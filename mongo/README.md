# MongoDB check

## Overview

Connect MongoDB to ServerDensity in order to:

* Visualize key MongoDB metrics.
* Correlate MongoDB performance with the rest of your applications.

## Setup
### Installation

Ensure the sd-agent repository is configured on your server, install the `sd-agent-mongo` package.

### Configuration
#### Prepare MongoDB

In a Mongo shell, create a read-only user for the Server Density Agent in the `admin` database:

```
# Authenticate as the admin user.
use admin
db.auth("admin", "<YOUR_MONGODB_ADMIN_PASSWORD>")

# On MongoDB 2.x, use the addUser command.
db.addUser("serverdensity", "<UNIQUEPASSWORD>", true)

# On MongoDB 3.x or higher, use the createUser command.
db.createUser({
  "user":"serverdensity",
  "pwd": "<UNIQUEPASSWORD>",
  "roles" : [
    {role: 'read', db: 'admin' },
    {role: 'clusterMonitor', db: 'admin'},
    {role: 'read', db: 'local' }
  ]
})
```

#### Connect the Agent

Create a file `mongodb.yaml` in the Agent's `conf.d` directory. See the [sample mongodb.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/mongo/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - server: mongodb://serverdensity:<UNIQUEPASSWORD>@localhost:27017/admin
    additional_metrics:
      - collection       # collect metrics for each collection
      - metrics.commands
      - tcmalloc
      - top
```



Restart the Agent to start sending MongoDB metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `mongo` under the Checks section:

```
  Checks
  ======
    [...]

    mongo
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 1 event & 1 service check

    [...]
```

## Compatibility

The mongo check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

See the [MongoDB 3.0 Manual](https://docs.mongodb.org/manual/reference/command/dbStats/) for more detailed descriptions of some of these metrics.

**NOTE**: The following metrics are NOT collected by default:

|||
|---|---|
|metric prefix|what to add to `additional_metrics` to collect it|
|mongodb.collection|collection|
|mongodb.commands|top|
|mongodb.getmore|top|
|mongodb.insert|top|
|mongodb.queries|top|
|mongodb.readLock|top|
|mongodb.writeLock|top|
|mongodb.remove|top|
|mongodb.total|top|
|mongodb.update|top|
|mongodb.writeLock|top|
|mongodb.tcmalloc|tcmalloc|
|mongodb.metrics.commands|metrics.commands|
