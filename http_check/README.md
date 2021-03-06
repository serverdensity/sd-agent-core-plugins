# HTTP Integration

## Overview

Monitor the up/down status of local or remote HTTP endpoints. The HTTP check can detect bad response codes (e.g. 404), identify soon-to-expire SSL certificates, search responses for specific text, and much more. The check also submits HTTP response times as a metric.

## Setup
### Installation

The HTTP-Status check can be installed with your package manager, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=http+status). Though many metrics-oriented checks are best run on the same host(s) as the monitored service, you may want to run this status-oriented check from hosts that do not run the monitored sites.



### Configuration

Create a file `http_check.yaml` in the Agent's `conf.d` directory. See the [sample http_check.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/http_check/conf.yaml.example) for all available configuration options:

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

See the [sample http_check.yaml](conf.yaml.example) for a full list and description of available options, here is a list of them:

| Setting | Description |
|---|---|
| `name` | The name associated with this instance/URL. This will be presented as a tag on the Service Checks and Metrics. Note: This name tag will have any spaces or dashes converted to underscores. |
| `url` | The URL to test. |
| `timeout` | The time in seconds to allow for a response. |
| `method` | The HTTP method. This setting defaults to GET, though many other HTTP methods are supported, including POST and PUT. |
| `data` | The data option is only available when using the POST method. Data should be included as key-value pairs and will be sent in the body of the request. |
| `content_match` | A string or Python regular expression. The HTTP check will search for this value in the response and will report as DOWN if the string or expression is not found. |
| `reverse_content_match` | When true, reverses the behavior of the `content_match` option, i.e. the HTTP check will report as DOWN if the string or expression in `content_match` IS found. (default is false)|
| `username` & `password` | If your service uses basic authentication, you can provide the username and password here. |
| `http_response_status_code` | A string or Python regular expression for an HTTP status code. This check will report DOWN for any status code that does not match. This defaults to 1xx, 2xx and 3xx HTTP status codes. For example: `401` or `4\d\d`.|
| `include_content` | When set to `true`, the check will include the first 200 characters of the HTTP response body in notifications. The default value is `false`. |
| `collect_response_time` | By default, the check will collect the response time (in seconds) as the metric `network.http.response_time`. To disable, set this value to `false`. |
| `disable_ssl_validation` | This setting will skip SSL certificate validation and is enabled by default. If you require SSL certificate validation, set this to `false`. |
| `ignore_ssl_warning` | When SSL certificate validation is enabled (see setting above), this setting will allow you to disable security warnings. |
| `ca_certs` | This setting will allow you to override the default certificate path as specified in `init_config` |
| `check_certificate_expiration` | When `check_certificate_expiration` is enabled, the service check will check the expiration date of the SSL certificate. Note that this will cause the SSL certificate to be validated, regardless of the value of the `disable_ssl_validation` setting. |
| `days_warning` & `days_critical` | When `check_certificate_expiration` is enabled, these settings will raise a warning or critical alert when the SSL certificate is within the specified number of days from expiration. |
| `headers` | This parameter allows you to send additional headers with the request. Please see the [example YAML file](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/http_check/conf.yaml.example) for additional information and caveats. |
| `skip_event` | When enabled, the check will not create an event. This is useful to avoid duplicates with a server side service check. This defaults to `false`. |
| `no_proxy` | If set, the check will bypass proxy settings and attempt to reach the check url directly. This defaults to `false`. |
| `allow_redirects` | This setting allows the service check to follow HTTP redirects and defaults to `true`.
| `tags` | A list of arbitrary tags that will be associated with the check. |

When you have finished configuring `http_check.yaml`, restart the Agent to begin sending HTTP response times to Server Density.

### Validation

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

## Compatibility

The http_check check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.
