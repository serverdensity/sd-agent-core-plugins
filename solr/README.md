# Solr Check

# Overview

The Solr check tracks the state and performance of a Solr cluster. It collects metrics like number of documents indexed, cache hits and evictions, average request times, average requests per second, and more.

# Installation

The Solr check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=solr). To install the Solr check install the `sd-agent-solr` package.

This check is JMX-based, so you'll need to enable JMX Remote on your Tomcat servers. Read the [JMX Check documentation](hhttps://support.serverdensity.com/hc/en-us/search?query=java) for more information on that.

# Configuration

Create a file `solr.yaml` in the Agent's `conf.d` directory:

```
instances:
# location of tomcat
  - host: localhost
    port: 9999

# if tomcat requires authentication
#   user: <TOMCAT_USERNAME>
#   password: <TOMCAT_PASSWORD>

init_config:
  conf:
    - include:
      type: searcher
      attribute:
        maxDoc:
          alias: solr.searcher.maxdoc
          metric_type: gauge
        numDocs:
          alias: solr.searcher.numdocs
          metric_type: gauge
        warmupTime:
          alias: solr.searcher.warmup
          metric_type: gauge
    - include:
      id: org.apache.solr.search.FastLRUCache
      attribute:
        cumulative_lookups:
          alias: solr.cache.lookups
          metric_type: counter
        cumulative_hits:
          alias: solr.cache.hits
          metric_type: counter
        cumulative_inserts:
          alias: solr.cache.inserts
          metric_type: counter
        cumulative_evictions:
          alias: solr.cache.evictions
          metric_type: counter
    - include:
      id: org.apache.solr.search.LRUCache
      attribute:
        cumulative_lookups:
          alias: solr.cache.lookups
          metric_type: counter
        cumulative_hits:
          alias: solr.cache.hits
          metric_type: counter
        cumulative_inserts:
          alias: solr.cache.inserts
          metric_type: counter
        cumulative_evictions:
          alias: solr.cache.evictions
          metric_type: counter
    - include:
      id: org.apache.solr.handler.component.SearchHandler
      attribute:
        errors:
          alias: solr.search_handler.errors
          metric_type: counter
        requests:
          alias: solr.search_handler.requests
          metric_type: counter
        timeouts:
          alias: solr.search_handler.timeouts
          metric_type: counter
        totalTime:
          alias: solr.search_handler.time
          metric_type: counter
        avgTimePerRequest:
          alias: solr.search_handler.avg_time_per_req
          metric_type: gauge
        avgRequestsPerSecond:
          alias: solr.search_handler.avg_requests_per_sec
          metric_type: gauge
```


Restart the Agent to start sending Solr metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `solr` under the Checks section:

```
  Checks
  ======
    [...]

    solr
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 0 service checks

    [...]
```

# Compatibility

The solr check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.
