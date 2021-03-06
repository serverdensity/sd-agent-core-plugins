# CouchDB Integration
{{< img src="integrations/couchdb/couchdb_graph.png" alt="CouchDb Graph" responsive="true" popup="true">}}
## Overview

Capture CouchDB data to:

* Visualize key CouchDB metrics.
* Correlate CouchDB performance with the rest of your applications.

For performance reasons, the CouchDB version you're using is cached, so you cannot monitor CouchDB instances with different versions with the same agent instance.

## Setup
### Installation

The CouchDB check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=couchdb). To install the couchdb check install the `sd-agent-couchdb` package.

### Configuration

Create a file `couch.yaml` in the Agent's `conf.d` directory. See the [sample  couch.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/couch/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - server: http://localhost:5984 # or wherever your CouchDB is listening
  #user: <your_username>
  #password: <your_password>
  #name: <A node's Erlang name> # Only for CouchDB 2.x
  #max_nodes_per_check: If no name is specified, the agent will scan all nodes up. As that may be very long, you can limit how many to collect per check. Default: 20
  #max_dbs_per_check. Maximum number of databases to report on. Default: 50
```

Optionally, provide a `db_whitelist` and `db_blacklist` to control which databases the Agent should and should not collect metrics from.

Restart the Agent to begin sending CouchDB metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `couch` under the Checks section:

```
  Checks
  ======
    [...]

    couch
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
