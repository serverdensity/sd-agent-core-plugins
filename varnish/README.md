# Varnish Integration

## Overview

Connect Varnish to Server Density in order to:

* Visualize your cache performance in real-time
* Correlate the performance of Varnish with the rest of your applications

## Installation

Install the `sd-agent-varnish` package manually or with your favorite configuration manager

## Configuration

Configure the Agent to connect to Varnish

 - Edit conf.d/varnish.yaml
```
init_config:

instances:
    - varnishstat: /usr/bin/varnishstat
      tags:
          - instance:production
```

 - If you're running Varnish 4.1+, you must add the sd-agent user to the varnish group.
```
sudo usermod -a -G varnish sd-agent
```

## Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        varnish
        -------
          - instance #0 [OK]
          - Collected 8 metrics & 0 events

## Compatibility

The Varnish check is compatible with all major platforms
