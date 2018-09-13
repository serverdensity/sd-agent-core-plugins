# SNMP Check

## Overview

This check lets you collect SNMP metrics from your network devices.

## Setup
### Installation

The SNMP check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=snmp). To install the SNMP check install the `sd-agent-snmp` package.

### Configuration

The SNMP check doesn't collect anything by default; you have to tell it specifically what to collect.

Here's an example `snmp.yaml`. See the [sample snmp.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/snmp/conf.yaml.example) for all available configuration options:

```
init_config:
   - mibs_folder: /path/to/your/additional/mibs

instances:
   - ip_address: localhost
     port: 161
     community_string: public
#    snmp_version: 1 # set to 1 if your devices use SNMP v1; no need to set otherwise, the default is 2
     timeout: 1      # in seconds; default is 1
     retries: 5
#    enforce_mib_constraints: false # set to false to NOT verify that returned values meet MIB constraints; default is true
     metrics:
       - MIB: UDP-MIB
         symbol: udpInDatagrams
       - OID: 1.3.6.1.2.1.6.5
         name: tcpPassiveOpens
       - MIB: IF-MIB
         table: ifTable
         symbols:
           - ifInOctets
           - ifOutOctets
         metric_tags:
           - tag: interface
             column: ifDescr
```

List each SNMP device as a distinct instance, and for each instance, list any SNMP counters and gauges you like in the `metrics` option. There are a few ways to specify what metrics to collect.

#### MIB and symbol

```
    metrics:
      - MIB: UDP-MIB
        symbol: udpInDatagrams
```

#### OID and name

```
    metrics:
      - OID: 1.3.6.1.2.1.6.5
        name: tcpActiveOpens # what to use in the metric name; can be anything
```

#### MIB and table

```
    metrics:
      - MIB: IF-MIB
        table: ifTable
        symbols:
          - ifInOctets      # row whose value becomes metric value
        metric_tags:
          - tag: interface  # tag name
            column: ifDescr # the column name to get the tag value from, OR
            #index: 1       # the column index to get the tag value from
```

This lets you collect metrics on all rows in a table (`symbols`) and specify how to tag each metric (`metric_tags`).

#### Use your own MIB

The SNMP check can collect MIB data that is formatted via [pysnmp](https://pypi.python.org/pypi/pysnmp). You can use the `build-pysnmp-mibs` script that ships with pysnmp to generate such data.

Put all your pysnmp MIBs into any directory and point the SNMP check to this directory: set `mibs_folder: <your_mibs_folder>` under the `init_config` section of `snmp.yaml`.

---

Restart the Agent to start sending SNMP metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `snmp` under the Checks section:

```
  Checks
  ======
    [...]

    snmp
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The snmp check is compatible with all major platforms.

## Data Collected
### Metrics

The SNMP check will submits specified metrics under the `snmp.*` namespace.

### Knowledge Base

Our agent allows you to monitor the SNMP Counters and Gauge of your choice. Specify for each device the metrics that you want to monitor in the ```metrics``` subsection using one of the following methods:

#### Specify a MIB and the symbol that you want to export

    metrics:
      - MIB: UDP-MIB
        symbol: udpInDatagrams

#### Specify an OID and the name you want the metric to appear under in Server Density

    metrics:
      - OID: 1.3.6.1.2.1.6.5
        name: tcpActiveOpens

*The name here is the one specified in the MIB but you could use any name.*

#### Specify a MIB and a table you want to extract information from

    metrics:
      - MIB: IF-MIB
        table: ifTable
        symbols:
          - ifInOctets
        metric_tags:
          - tag: interface
        column: ifDescr

This allows you to gather information on all the table's row, as well as to specify tags to gather.

Use the ```symbols``` list to specify the metric to gather and the ```metric_tags``` list to specify the name of the tags and the source to use.

In this example the agent would gather the rate of octets received on each interface and tag it with the interface name (found in the ifDescr column), resulting in a tag such as ```interface:eth0```

    metrics:
      - MIB: IP-MIB
        table: ipSystemStatsTable
        symbols:
          - ipSystemStatsInReceives
        metric_tags:
          - tag: ipversion
        index: 1

You can also gather tags based on the indices of your row, in case they are meaningful. In this example, the first row index contains the ip version that the row describes (ipv4 vs. ipv6)

#### Use your own Mib

To use your own MIB with the sd-agent, you need to convert them to the pysnmp format. This can be done using the ```build-pysnmp-mibs``` script that ships with pysnmp.

It has a dependency on ```smidump```, from the libsmi2ldbl package so make sure it is installed. Make also sure that you have all the dependencies of your MIB in your mib folder or it won't be able to convert your MIB correctly.

##### Run

    $ build-pysnmp-mib -o YOUR-MIB.py YOUR-MIB.mib

where YOUR-MIB.mib is the MIB you want to convert.

Put all your pysnmp mibs into a folder and specify this folder's path in ```snmp.yaml``` file, in the ```init_config``` section.
