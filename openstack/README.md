# Openstack Integration
## Overview

Get metrics from openstack service in real time to:

* Visualize and monitor openstack states
* Be notified about openstack failovers and events.

## Setup
### Installation

Install the `sd-agent-openstack` package manually or with your favorite configuration manager


### Configuration

To capture OpenStack metrics you need to install the sd-agent on your hosts running hypervisors.

1. First configure a Server Density role and user with your identity server


        openstack role create sd_agent
        openstack user create serverdensity \
            --password my_password \
            --project my_project_name
        openstack role add sd_agent \
            --project my_project_name \
            --user serverdensity


2. Update your policy.json files to grant the needed permissions.
```role:sd_agent``` requires access to the following operations:

**Nova**

```json
{
    "compute_extension": "aggregates",
    "compute_extension": "hypervisors",
    "compute_extension": "server_diagnostics",
    "compute_extension": "v3:os-hypervisors",
    "compute_extension": "v3:os-server-diagnostics",
    "compute_extension": "availability_zone:detail",
    "compute_extension": "v3:availability_zone:detail",
    "compute_extension": "used_limits_for_admin",
    "os_compute_api:os-aggregates:index": "rule:admin_api or role:sd_agent",
    "os_compute_api:os-aggregates:show": "rule:admin_api or role:sd_agent",
    "os_compute_api:os-hypervisors": "rule:admin_api or role:sd_agent",
    "os_compute_api:os-server-diagnostics": "rule:admin_api or role:sd_agent",
    "os_compute_api:os-used-limits": "rule:admin_api or role:sd_agent"
}
```

**Neutron**

```json
{
    "get_network": "rule:admin_or_owner or rule:shared or rule:external or rule:context_is_advsvc or role:sd_agent"
}
```

**Keystone**

```json
{
    "identity:get_project": "rule:admin_required or project_id:%(target.project.id)s or role:sd_agent",
    "identity:list_projects": "rule:admin_required or role:sd_agent"
}
```

You may need to restart your Keystone, Neutron and Nova API services to ensure that the policy changes take.


3. Configure the Server Density Agent to connect to your Keystone server, and specify individual projects to monitor. Edit `openstack.yaml`. You can find a sample configuration in the conf.d directory in your agent install. See the [sample openstack.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/openstack/conf.yaml.example) for all available configuration options.

4. Restart the Agent

### Validation

When you run execute the info subcommand you should see something like the following:

    Checks
    ======

        openstack
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The openstack check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
