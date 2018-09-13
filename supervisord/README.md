# Agent Check: Supervisor
## Overview

This check monitors the uptime, status, and number of processes running under supervisord.

## Setup
### Installation

The supervisor check can be installed with your package manager, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=supervisor). install the `sd-agent-supervisord` package.

### Configuration
#### Prepare supervisord

The Agent can collect data from Supervisor via HTTP server or UNIX socket. The Agent collects the same data no matter which collection method you configure.
##### HTTP server

Add a block like this to supervisor's main configuration file (e.g. `/etc/supervisor.conf`):

```
[inet_http_server]
port=localhost:9001
username=user  # optional
password=pass  # optional
```

##### UNIX socket

Add blocks like these to `/etc/supervisor.conf` (if they're not already there):

```
[supervisorctl]
serverurl=unix:///var/run//supervisor.sock

[unix_http_server]
file=/var/run/supervisor.sock
chmod=777
```

If supervisor is running as root, make sure `chmod` is set so that non-root users (i.e. sd-agent) can read the socket.

---

Reload supervisord.

#### Connect the Agent

Create a file `supervisord.yaml` in the Agent's `conf.d` directory. See the [sample supervisord.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/supervisord/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - name: supervisord0 # used to tag service checks and metrics, i.e. supervisor_server:supervisord0
    host: localhost
    port: 9001

# To collect from the socket instead
# - name: supervisord0
#   host: http://127.0.0.1
#   socket: unix:///var/run//supervisor.sock
```

Use the `proc_names` and/or `proc_regex` options to list processes you want the Agent to collect metrics on and create service checks for. If you don't provide either option, the Agent tracks _all_ child processes of supervisord. If you provide both options, the Agent tracks processes from both lists (i.e. the two options are not mutually exclusive).


Configuration Options

* `name` (Required) - An arbitrary name to identify the supervisord server.
* `host` (Optional) - Defaults to localhost. The host where supervisord server is running.
* `port` (Optional) - Defaults to 9001. The port number.
* `user` (Optional) - Username
* `pass` (Optional) - Password
* `proc_names` (Optional) - Dictionary of process names to monitor
* `server_check` (Optional) - Defaults to true. Service check for connection to supervisord server.
* `socket` (Optional) - If using supervisorctl to communicate with supervisor, a socket is needed.

See the [example check configuration](conf.yaml.example) for comprehensive descriptions of other check options.

Restart the Agent to start sending Supervisor metrics to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `supervisord` under the Checks section:

```
  Checks
  ======
    [...]

    supervisord
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 4 service check

    [...]
```

## Compatibility

The supervisord check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

