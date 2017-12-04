# Jenkins Integration

## Overview

Get metrics from jenkins service in real time to:

* Visualize and monitor jenkins states

## Installation

Install the `sd-check-jenkins` package manually or with your favorite configuration manager

## Configuration

Edit the `jenkins.yaml` file to point to your server and port, set the masters to monitor

## Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        jenkins
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The jenkins check is compatible with all major platforms