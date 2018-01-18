# Openstack Integration
{{< img src="integrations/openstack/openstack.png" alt="OpenStack default dashboard" responsive="true" popup="true">}}
## Overview

Get metrics from openstack service in real time to:

* Visualize and monitor openstack states
* Be notified about openstack failovers and events.

## Setup
### Installation

Install the `sd-agent-openstack` package manually or with your favorite configuration manager

Installing the OpenStack Integration could increase the number of VMs that Datadog monitors. For more information on how this may affect your billing, please visit our Billing FAQ.

### Configuration

To capture OpenStack metrics you need to install the Datadog Agent on your hosts running hypervisors.

1. First configure a Datadog role and user with your identity server


        openstack role create datadog_monitoring
        openstack user create datadog \
            --password my_password \
            --project my_project_name
        openstack role add datadog_monitoring \
            --project my_project_name \
            --user datadog


2. Update your policy.json files to grant the needed permissions.
```role:datadog_monitoring``` requires access to the following operations:

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
    "os_compute_api:os-aggregates:index": "rule:admin_api or role:datadog_monitoring",
    "os_compute_api:os-aggregates:show": "rule:admin_api or role:datadog_monitoring",
    "os_compute_api:os-hypervisors": "rule:admin_api or role:datadog_monitoring",
    "os_compute_api:os-server-diagnostics": "rule:admin_api or role:datadog_monitoring",
    "os_compute_api:os-used-limits": "rule:admin_api or role:datadog_monitoring"
}
```

**Neutron**

```json
{
    "get_network": "rule:admin_or_owner or rule:shared or rule:external or rule:context_is_advsvc or role:datadog_monitoring"
}
```

**Keystone**

```json
{
    "identity:get_project": "rule:admin_required or project_id:%(target.project.id)s or role:datadog_monitoring",
    "identity:list_projects": "rule:admin_required or role:datadog_monitoring"
}
```

You may need to restart your Keystone, Neutron and Nova API services to ensure that the policy changes take.


3. Configure the Datadog Agent to connect to your Keystone server, and specify individual projects to monitor. Edit `openstack.yaml`. You can find a sample configuration in the conf.d directory in your agent install. See the [sample openstack.yaml](https://github.com/DataDog/integrations-core/blob/master/openstack/conf.yaml.example) for all available configuration options.

4. [Restart the Agent](https://docs.datadoghq.com/agent/faq/start-stop-restart-the-datadog-agent)

### Validation

When you run `sd-agent info` you should see something like the following:

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
