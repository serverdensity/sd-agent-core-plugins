# Process Check

## Overview

The process check lets you:

* Collect resource usage metrics for specific running processes on any host: CPU, memory, I/O, number of threads, etc
* Use Process Monitors: configure thresholds for how many instances of a specific process ought to be running and get alerts when the thresholds aren't met (see **Service Checks** below).

## Setup
### Installation
Install the `sd-agent-process` package manually or with your favorite configuration manager

### Configuration

Unlike many checks, the process check doesn't monitor anything useful by default; you must tell it which processes you want to monitor, and how.

While there's no standard default check configuration, here's an example `process.yaml` that monitors ssh/sshd processes. See the [sample process.yaml](conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - name: ssh
    search_string: ['ssh', 'sshd']

# To search for sshd processes using an exact cmdline
# - name: ssh
#   search_string: ['/usr/sbin/sshd -D']
#   exact_match: True
```

You can also configure the check to find any process by exact PID (`pid`) or pidfile (`pid_file`). If you provide more than one of `search_string`, `pid`, and `pid_file`, the check will the first option it finds in that order (e.g. it uses `search_string` over `pid_file` if you configure both).

To have the check search for processes in a path other than `/proc`, set `procfs_path: <your_proc_path>` in `config.cfg`, NOT in `process.yaml` (its use has been deprecated there). Set this to `/host/proc` if you're running the Agent from a Docker container (i.e. [docker-sd-agent](https://github.com/serverdensity/docker-sd-agent)) and want to monitor processes running on the server hosting your containers. You DON'T need to set this to monitor processes running _in_ your containers; the [Docker check](https://github.com/serverdensity/sd-agent-core-plugins/tree/master/docker_daemon) monitors those.

See the [example configuration](conf.yaml.example) for more details on configuration options.

```sudo /etc/init.d/sd-agent restart```

### Validation

When you run `sd-agent info` you should see something like the following:

```
  Checks
  ======
    [...]

    process
    -------
      - instance #0 [OK]
      - instance #1 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

Each instance configured in `process.yaml` should have one `instance #<num> [OK]` line in the output, regardless of how many search_strings it might be configured with.

## Compatibility

The process check is compatible with all major platforms.

## Data Collected
### Metrics

**Note**: Some metrics are not available on Linux or OSX:

* Process I/O metrics aren't available on Linux or OSX since the files that the agent must read (/proc//io) are only readable by the process's owner. F
* `system.cpu.iowait` is not available on windows

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

All metrics are per `instance` configured in process.yaml, and are tagged `process_name:<instance_name>`.

