# Mesos_master Check

## Overview

This check collects metrics from Mesos masters for:

* Cluster resources
* Slaves registered, active, inactive, connected, disconnected, etc
* Number of tasks failed, finished, staged, running, etc
* Number of frameworks active, inactive, connected, and disconnected

And many more.
## Setup
### Installation
The installation is the same on Mesos with and without DC/OS.
Run the docker sd-agent container on each of your Mesos master nodes:

docker run -d --name sd-agent -v /var/run/docker.sock:/var/run/docker.sock -v /proc/:/host/proc/:ro -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro -e AGENT_KEY=$AGENT_KEY -e ACCOUNT=$ACCOUNT serverdensity/sd-agent

```
docker run -d --name sd-agent \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /proc/:/host/proc/:ro \
  -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
  -e AGENT_KEY=$AGENT_KEY \
  -e ACCOUNT=$ACCOUNT \
  -e MESOS_MASTER=yes \
  -e MARATHON_URL=http://leader.mesos:8080 \
  -e SD_BACKEND=docker \
  serverdensity/sd-agent:latest
```

Substitute your Server Density agent key, account and Mesos Master's API URL into the command above.

### Configuration

If you passed the correct Master URL when starting the sd-agent container, the Agent is already using a default `mesos_master.yaml` to collect metrics from your masters; you don't need to configure anything else. See the [sample mesos_master.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/mesos_master/conf.yaml.example) for all available configuration options.

Unless your masters' API uses a self-signed certificate. In that case, set `disable_ssl_validation: true` in `mesos_master.yaml`.

### Validation

In your Server Density account, search for `mesos.cluster` metrics.

## Compatibility

The mesos_master check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/mesos_master/metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).

