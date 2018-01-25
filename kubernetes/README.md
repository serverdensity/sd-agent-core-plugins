# Kubernetes Integration
## Overview

Get metrics from kubernetes service in real time to:

* Visualize and monitor kubernetes states
* Be notified about kubernetes failovers and events.

## Setup
### Installation

Install the `sd-agent-kubernetes` package manually or with your favorite configuration manager

### Configuration

Edit the `kubernetes.yaml` file to point to your server and port, set the masters to monitor. See the [sample kubernetes.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/kubernetes/conf.yaml.example) for all available configuration options.

### Validation

When you run `sd-agent info` you should see something like the following:

    Checks
    ======

        kubernetes
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The kubernetes check is compatible with all major platforms

## Data Collected
### Metrics
See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

## Troubleshooting
### Can I install the agent on my Kubernetes master node(s) ?
Yes, since Kubernetes 1.6, the concept of [Taints and tolerations](http://blog.kubernetes.io/2017/03/advanced-scheduling-in-kubernetes.html) was introduced. Now rather than the master being off limits, it's simply tainted.  Add the required toleration to the pod to run it:

Add the following lines to your Deployment (or Daemonset if you are running a multi-master setup):
```
spec:
 tolerations:
 - key: node-role.kubernetes.io/master
   effect: NoSchedule
```

### Why is the Kubernetes check failing with a ConnectTimeout error to port 10250?
The agent assumes that the kubelet API is available at the default gateway of the container. If that's not the case because you are using a software defined networks like Calico or Flannel, the agent needs to be specified using an environment variable:
```
          - name: KUBERNETES_KUBELET_HOST
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
```

###  Why is there a container in each Kubernetes pod with 0% CPU and minimal disk/ram?
These are pause containers (docker_image:gcr.io/google_containers/pause.*) that K8s injects into every pod to keep it populated even if the "real” container is restarting/stopped.

The docker_daemon check ignores them through a default exclusion list, but they will show up for K8s metrics like *kubernetes.cpu.usage.total* and *kubernetes.filesystem.usage*.

