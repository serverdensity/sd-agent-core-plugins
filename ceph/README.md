# Ceph Integration

# Overview

Enable the Ceph integration to:

  * Track disk usage across storage pools
  * Receive service checks in case of issues
  * Monitor I/O performance metrics

# Installation

The Ceph check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=ceph). To install the ceph check install the `sd-agent-ceph` package.

# Configuration

Create a file `ceph.yaml` in the Agent's `conf.d` directory:

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

# Validation

Run the Agent's `info` subcommand and look for `ceph` under the Checks section:

```
  Checks
  ======
    [...]

    ceph
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Troubleshooting

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
