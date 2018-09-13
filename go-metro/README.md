# Agent Check: TCP RTT (go-metro)

## Overview

The TCP RTT check reports on roundtrip times between the host the agent is running on and any host it is communicating with. This check is passive and will only report RTT times for packets being sent and received from outside the check. The check itself will not send any packets.

This check is only available in 64-bit DEB and RPM sd-agent packages.

## Setup
### Installation

The TCP RTT check—also known as go-metro is in the `sd-agent-go-metro` package from the sd-agent repository, but requires additional system libraries. The check uses timestamps provided by the PCAP library to compute the time between any outgoing packet and the corresponding TCP acknowledgement. As such, PCAP must be installed and configured.

Debian-based systems should use one of the following:

```
$ sudo apt-get install libcap
$ sudo apt-get install libcap2-bin
```

Redhat-based systems should use one of these:

```
$ sudo yum install libcap
$ sudo yum install compat-libcap1
```

Finally, configure PCAP:

```
$ sudo setcap cap_net_raw+ep /usr/share/python/sd-agent/bin/go-metro
```

### Configuration

Edit the ```go-metro.yaml``` file in your agent's ```conf.d``` directory. See the [sample go-metro.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/go-metro/conf.yaml.example) for all available configuration options. The following is an example file that will show the TCP RTT times for serverdensity.com and 192.168.0.22:

    init_config:
      snaplen: 512
      idle_ttl: 300
      exp_ttl: 60
      statsd_ip: 127.0.0.1
      statsd_port: 8125
      log_to_file: true
      log_level: info

    instances:
      - interface: eth0
        tags:
          - env:prod
        ips:
          - 45.33.125.153
        hosts:
          - serverdensity.com

### Validation

To validate that the check is running correctly, you should see `system.net.tcp.rtt` metrics showing in the Server Density interface. Also, if you run `sudo /etc/init.d/sd-agent status`, you should see something similar to the following:

    ● sd-agent.service - LSB: Start and stop sd-agent
       Loaded: loaded (/etc/rc.d/init.d/sd-agent; bad; vendor preset: disabled)
       Active: active (running) since Fri 2017-12-22 17:25:50 UTC; 1 months 4 days ago
         Docs: man:systemd-sysv-generator(8)
       Memory: 132.5M
       CGroup: /system.slice/sd-agent.service
               ├─ 1847 mpstat -P ALL 1 1
               ├─30737 /usr/share/python/sd-agent/bin/python /usr/share/python/sd-agent/bin/supervisord -c /etc/sd-agent/supervisor.conf
               ├─30739 /usr/share/python/sd-agent/bin/python /usr/share/python/sd-agent/sdagent.py
               ├─30740 /usr/share/python/sd-agent/bin/python /usr/share/python/sd-agent/agent.py foreground --use-local-forwarder
               └─30741 /usr/share/python/sd-agent/bin/go-metro -cfg=/etc/sd-agent/conf.d/go-metro.yaml

If the TCP RTT check has started you should see something similar to the go-metro line above.

This is a passive check, so unless there are packets actively being sent to the hosts mentioned in the yaml file, the metrics will not be reported.

## Compatibility

The TCP RTT check is compatible with Linux platforms.

## Data Collected
### Metrics

See [metadata.csv](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/go-metro/metadata.csv) for a list of metrics provided by this check.

## Troubleshooting
Need help? Contact [Server Density Support](http://support.serverdensity.com).
