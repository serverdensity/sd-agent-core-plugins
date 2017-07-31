# Kube-dns Integration

## Overview

Get metrics from kube-dns service in real time to:

* Visualize and monitor dns metrics collected via Kubernetes' kube-dns addon
  through Prometheus

See https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/dns for
more informations about kube-dns

## Installation

The Kube-dns check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=kube+dns). To install the kube-dns check install the `sd-agent-kube-dns` package.

## Configuration

Edit the `kube_dns.yaml` file to point to your server and port, set the masters to monitor


## Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        kube_dns
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The kube_dns check is compatible with all major platforms
