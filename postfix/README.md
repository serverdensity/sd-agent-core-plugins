# Postfix Check
{{< img src="integrations/postfix/postfixgraph.png" alt="Postfix Graph" responsive="true" popup="true">}}
## Overview

This check monitors the size of all your Postfix queues.

## Setup
### Installation

The Postfix check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=Postfix). To install the Postfix check install the `sd-agent-postfix` package.

## Configuration
This check can be configured to use the `find` command which requires granting the dd-agent user sudo access to get a count of messages in the `incoming`, `active`, and `deferred` mail queues.

Optionally, you can configure the agent to use a built in `postqueue -p` command to get a count of messages in the `active`, `hold`, and `deferred` mail queues. `postqueue` is exectued with set-group ID privileges without the need for sudo.

**WARNING**: Using `postqueue` to monitor the mail queues will not report a count of messages for the `incoming` queue.

### Using sudo
Create a file `postfix.yaml` in the Agent's `conf.d` directory. See the [sample postfix.yaml](https://github.com/DataDog/integrations-core/blob/master/postfix/conf.yaml.example) for all available configuration options:

```
init_config:
  postfix_user: postfix

instances:
  # add one instance for each postfix service you want to track
  - directory: /var/spool/postfix
    queues:
      - incoming
      - active
      - deferred
#   tags:
#     - optional_tag1
#     - optional_tag2
```

For each mail queue in `queues`, the Agent forks a `find` on its directory.
It uses `sudo` to do this with the privileges of the postfix user, so you must
add the following lines to `/etc/sudoers` for the Agent's user, `sd-agent`,
assuming postfix runs as `postfix`:
```
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/incoming -type f
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/active -type f
sd-agent ALL=(postfix) NOPASSWD:/usr/bin/find /var/spool/postfix/deferred -type f
```
### Using postqueue
Create a file `postfix.yaml` in the Agent's `conf.d` directory:

```
init_config:
  postqueue: true

instances:
  # The config_directory option only applies when `postqueue: true`.
  # The config_directory is the location of the Postfix configuration directory
  # where main.cf lives.
  - config_directory: /etc/postfix
#   tags:
#     - optional_tag
#     - optional_tag0
```
For each `config_directory` in `instances`, the Agent forks a `postqueue -c` for
the Postfix configuration directory.

Postfix has internal access controls that limit activities on the mail queue. By default,
Postfix allows `anyone` to view the queue. On production systems where the Postfix installation
may be configured with stricter access controls, you may need to grant the dd-agent user access to view
the mail queue.

Run the Agent's `info` subcommand and look for postfix under the Checks section:
    
    postconf -e "authorized_mailq_users = sd-agent"        

http://www.postfix.org/postqueue.1.html

            authorized_mailq_users (static:anyone)
                List of users who are authorized to view the queue.


[Restart the Agent](https://docs.datadoghq.com/agent/faq/start-stop-restart-the-datadog-agent) to start sending Postfix metrics to Datadog.

### Validation

Restart the Agent to start sending Postfix metrics to Server Density.

```
  Checks
  ======
    [...]

    postfix
    -------
      - instance #0 [OK]
      - Collected 3 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The postfix check is compatible with all major platforms.

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

