# HTTP Integration

# Overview

Monitor the up/down status of local or remote HTTP endpoints. The HTTP check can detect bad response codes (e.g. 404), identify soon-to-expire SSL certificates, search responses for specific text, and much more. The check also submits HTTP response times as a metric.

# Installation

The HTTP-Status check can be installed with your package manager, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=http+status). Though many metrics-oriented checks are best run on the same host(s) as the monitored service, you may want to run this status-oriented check from hosts that do not run the monitored sites.



# Configuration

Create a file `http_check.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - name: Example website
    url: https://example.com/
    # disable_ssl_validation: false      # default is true, so set false to check SSL validation
    # ca_certs: /path/to/ca/file         # e.g. /etc/ssl/certs/ca-certificates.crt
    # check_certificate_expiration: true # default is true
    # days_warning: 28                   # default 14
    # days_critical: 14                  # default 7
    # timeout: 3                         # in seconds. Default is 1.
    skip_event: true # Default is false, i.e. emit events instead of service checks. Recommend to set to true.
  - name: Example website (staging)
    url: http://staging.example.com/
    skip_event: true
```

The HTTP check has more configuration options than many checks — many more than are shown above. Most options are opt-in, e.g. the Agent will not check SSL validation unless you configure the requisite options. Notably, the Agent _will_ check for soon-to-expire SSL certificates by default.

See the [sample http_check.yaml](conf.yaml.example) for a full list and description of available options. There are options to send a POST (with data) instead of GET, set custom request headers, set desired response codes, and more.

When you have finished configuring `http_check.yaml`, restart the Agent to begin sending HTTP response times to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `http_check` under the Checks section:

```
  Checks
  ======
    [...]

    http_check
    ----------
      - instance #0 [WARNING]
          Warning: Skipping SSL certificate validation for https://example.com based on configuration
      - instance #1 [OK]
      - Collected 2 metrics, 0 events & 4 service checks

    [...]
```

# Troubleshooting

# Compatibility

The http_check check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
