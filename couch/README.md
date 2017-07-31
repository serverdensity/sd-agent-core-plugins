# CouchDB Integration

# Overview

Capture CouchDB data to:

* Visualize key CouchDB metrics.
* Correlate CouchDB performance with the rest of your applications.

# Installation

The CouchDB check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=couchdb). To install the couchdb check install the `sd-agent-couchdb` package.

# Configuration

Create a file `couch.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - server: http://localhost:5984 # or wherever your CouchDB is listening
  #user: <your_username>
  #password: <your_password>
```

Optionally, provide a `db_whitelist` and `db_blacklist` to control which databases the Agent should and should not collect metrics from.

Restart the Agent to begin sending CouchDB metrics to Server Density.

# Validation

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

# Troubleshooting

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
