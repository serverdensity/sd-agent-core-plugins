# Docker_daemon Integration
## Overview

Get metrics from docker_daemon service in real time to:

* Visualize and monitor docker_daemon states
* Be notified about docker_daemon failovers and events.

## Setup
### Installation

To collect Docker metrics about all your containers, you will run **one** Server Density Agent on every host. There are two ways to run the Agent: directly on each host, or within a [docker-sd-agent container](https://github.com/serverdensity/docker-sd-agent). We recommend the latter.

Whichever you choose, your hosts need to have cgroup memory management enabled for the Docker check to succeed.

#### Host Installation

1. Ensure Docker is running on the host.
2. Install the `sd-agent-docker` package manually or with your favorite configuration manager
3. Add the Agent user to the docker group: `usermod -a -G docker sd-agent`
4. Create a `docker_daemon.yaml` file by copying [the example file in the agent conf.d directory](https://github.com/serverdensity/sd-agent-core-/blob/master/docker_daemon/conf.yaml.example). If you have a standard install of Docker on your host, there shouldn't be anything you need to change to get the integration to work.
5. To enable other integrations, use `docker ps` to identify the ports used by the corresponding applications.

**Note:** docker_daemon has replaced the older docker integration.

#### Container Installation

1. Ensure Docker is running on the host.
2. Run:
      ```
      docker run -d --name sd-agent
      -v /var/run/docker.sock:/var/run/docker.sock
      -v /proc/:/host/proc/:ro
      -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
      -e AGENT_KEY=$YOUR_AGENT_KEY
      -e ACCOUNT=$YOUR_ACCOUNT
      serverdensity/sd-agent
      ```

Note that in the command above, you are able to pass your agent key and account name to the Server Density Agent using Docker's `-e` environment variable flag.

##### Full list of env variables
The following environment variables can be used when running the container:

* `AGENT_KEY` - Your agent key, can be found in your UI
* `ACCOUNT` - Your account name
* `LOG_LEVEL` - The log level of the agent running in the container
* `SD_HOSTNAME` - The hostname specified in your containered agent's config.cfg (Note that this does not set the container hostname)
* `PROXY_HOST` - Configures a proxy host for the agent
* `PROXY_PORT` - Configures a proxy port for the agent
* `PROXY_USER` - Configures a proxy user for the agent
* `PROXY_PASSWORD` - Configures a proxy password for the agent
* `CONTAINER_SIZE` - Set to `TRUE` to enable container size metrics
* `IMAGE_STATS` - Set to `TRUE` to enable image stat metrics
* `IMAGE_SIZE` - Set to `TRUE` to enable image size metrics
* `DISK_STATS` - Set to `TRUE` to enable disk stat metrics
* `TIMEOUT` - Set the timeout for the docker_daemon check in seconds


**Note**: Add `--restart=unless-stopped` if you want your agent to be resistant to restarts.


### Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        docker_daemon
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The docker_daemon check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

