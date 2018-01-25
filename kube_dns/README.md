# Kube-dns Integration

## Overview

Get metrics from kube-dns service in real time to:

* Visualize and monitor dns metrics collected via Kubernetes' kube-dns addon
  through Prometheus

See https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/dns for
more informations about kube-dns

## Setup
### Installation

The Kube-dns check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=kube+dns). To install the kube-dns check install the `sd-agent-kube-dns` package.

### Configuration

Edit the `kube_dns.yaml` file to point to your server and port, set the masters to monitor. See the [sample kube_dns.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/kube_dns/conf.yaml.example) for all available configuration options.

### Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        kube_dns
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The kube_dns check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

