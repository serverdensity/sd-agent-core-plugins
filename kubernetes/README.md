# Kubernetes Integration

## Overview

Get metrics from kubernetes service in real time to:

* Visualize and monitor kubernetes states
* Be notified about kubernetes failovers and events.

## Installation

Install the `sd-agent-kubernetes` package manually or with your favorite configuration manager

## Configuration

Edit the `kubernetes.yaml` file to point to your server and port, set the masters to monitor

## Validation

When you run `sd-agent info` you should see something like the following output. If you are on a systemd-based system, you should run `/usr/share/python/sd-agent/agent.py info` instead.

    Checks
    ======

        kubernetes
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The kubernetes check is compatible with all major platforms
