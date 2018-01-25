# Ceph Integration
## Overview

Enable the Ceph integration to:

  * Track disk usage across storage pools
  * Receive service checks in case of issues
  * Monitor I/O performance metrics

## Setup
### Installation

The Ceph check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=ceph). To install the ceph check install the `sd-agent-ceph` package.

### Configuration

Create a file `ceph.yaml` in the Agent's `conf.d` directory. See the [sample ceph.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/ceph/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - ceph_cmd: /path/to/your/ceph # default is /usr/bin/ceph
    use_sudo: true               # only if the ceph binary needs sudo on your nodes
```

If you enabled `use_sudo`, add a line like the following to your `sudoers` file:

```
sd-agent ALL=(ALL) NOPASSWD:/path/to/your/ceph
```

### Validation

Run the Agent's `info` subcommand and look for `ceph` under the Checks section:

```
  Checks
  ======
    [...]

   ceph (5.19.0)
   -------------
   - instance #0 [OK]
   - Collected 24 metrics, 0 events & 1 service check

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

Note: If you are running ceph luminous or later, you will not see the metric `ceph.osd.pct_used`.

