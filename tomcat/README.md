# Agent Check: Tomcat

## Overview

This check collects Tomcat metrics like:

* Overall activity metrics: error count, request count, processing times
* Thread pool metrics: thread count, number of threads busy
* Servlet processing times

And more.

## Setup
### Installation

The Tomcat check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=tomcat). To install the Tomcat check install the `sd-agent-tomcat` package.

This check is JMX-based, so you'll need to enable JMX Remote on your Tomcat servers. Follow the instructions in the [Tomcat documentation](http://tomcat.apache.org/tomcat-6.0-doc/monitoring.html) to do that.

### Configuration

Create a file `tomcat.yaml` in the Agent's `conf.d` directory. See the [sample tomcat.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/tomcat/conf.yaml.example) for all available configuration options:

```
instances:
    -   host: localhost
        port: 7199
        user: <TOMCAT_USERNAME>
        password: <PASSWORD>
        name: my_tomcat

init_config:
  conf:
    - include:
        type: ThreadPool
        attribute:
          maxThreads:
            alias: tomcat.threads.max
            metric_type: gauge
          currentThreadCount:
            alias: tomcat.threads.count
            metric_type: gauge
          currentThreadsBusy:
            alias: tomcat.threads.busy
            metric_type: gauge
    - include:
        type: GlobalRequestProcessor
        attribute:
          bytesSent:
            alias: tomcat.bytes_sent
            metric_type: counter
          bytesReceived:
            alias: tomcat.bytes_rcvd
            metric_type: counter
          errorCount:
            alias: tomcat.error_count
            metric_type: counter
          requestCount:
            alias: tomcat.request_count
            metric_type: counter
          maxTime:
            alias: tomcat.max_time
            metric_type: gauge
          processingTime:
            alias: tomcat.processing_time
            metric_type: counter
    - include:
        j2eeType: Servlet
        attribute:
          processingTime:
            alias: tomcat.servlet.processing_time
            metric_type: counter
          errorCount:
            alias: tomcat.servlet.error_count
            metric_type: counter
          requestCount:
            alias: tomcat.servlet.request_count
            metric_type: counter
    - include:
        type: Cache
        accessCount:
          alias: tomcat.cache.access_count
          metric_type: counter
        hitsCounts:
          alias: tomcat.cache.hits_count
          metric_type: counter
    - include:
        type: JspMonitor
        jspCount:
          alias: tomcat.jsp.count
          metric_type: counter
        jspReloadCount:
          alias: tomcat.jsp.reload_count
          metric_type: counter
```

See the [JMX Check documentation](https://support.serverdensity.com/hc/en-us/search?query=java) for a list of configuration options usable by all JMX-based checks. The page also describes how the Agent tags JMX metrics.

Restart the Agent to start sending Tomcat metrics to Server Density.

Configuration Options

* `user` and `password` (Optional) - Username and password.
* `process_name_regex` - (Optional) - Instead of specifying a host and port or jmx_url, the agent can connect using the attach api. This requires the JDK to be installed and the path to tools.jar to be set.
* `tools_jar_path` - (Optional) - To be set when process_name_regex is set.
* `java_bin_path` - (Optional) - Should be set if the agent cannot find your java executable.
* `java_options` - (Optional) - Java JVM options
* `trust_store_path` and `trust_store_password` - (Optional) - Should be set if ssl is enabled.

The `conf` parameter is a list of dictionaries. Only 2 keys are allowed in this dictionary:

* `include` (**mandatory**): Dictionary of filters, any attribute that matches these filters will be collected unless it also matches the "exclude" filters (see below)
* `exclude` (**optional**): Another dictionary of filters. Attributes that match these filters won't be collected

For a given bean, metrics get tagged in the following manner:

    mydomain:attr0=val0,attr1=val1

Your metric will be mydomain (or some variation depending on the attribute inside the bean) and have the tags `attr0:val0, attr1:val1, domain:mydomain`.

If you specify an alias in an `include` key that is formatted as *camel case*, it will be converted to *snake case*. For example, `MyMetricName` will be shown in Server Density as `my_metric_name`.

#### The `attribute` filter

The `attribute` filter can accept two types of values:

* A dictionary whose keys are attributes names:

      conf:
        - include:
            attribute:
              maxThreads:
                alias: tomcat.threads.max
                metric_type: gauge
              currentThreadCount:
                alias: tomcat.threads.count
                metric_type: gauge
              bytesReceived:
                alias: tomcat.bytes_rcvd
                metric_type: counter

In that case you can specify an alias for the metric that will become the metric name in Server Density. You can also specify the metric type either a gauge or a counter. If you choose counter, a rate per second will be computed for this metric.

* A list of attributes names:

      conf:
        - include:
            domain: org.apache.cassandra.db
            attribute:
              - BloomFilterDiskSpaceUsed
              - BloomFilterFalsePositives
              - BloomFilterFalseRatio
              - Capacity
              - CompressionRatio
              - CompletedTasks
              - ExceptionCount
              - Hits
              - RecentHitRate

In that case:

  * The metric type will be a gauge
  * The metric name will be jmx.\[DOMAIN_NAME].\[ATTRIBUTE_NAME]

Here is another filtering example:

    instances:
      - host: 127.0.0.1
        name: jmx_instance
        port: 9999

    init_config:
      conf:
        - include:
            bean: org.apache.cassandra.metrics:type=ClientRequest,scope=Write,name=Latency
            attribute:
              - OneMinuteRate
              - 75thPercentile
              - 95thPercentile
              - 99thPercentile


### Validation

Run the Agent's `info` subcommand and look for `tomcat` under the Checks section:

```
  Checks
  ======
    [...]

    tomcat
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 0 service checks

    [...]
```

## Compatibility

The tomcat check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

