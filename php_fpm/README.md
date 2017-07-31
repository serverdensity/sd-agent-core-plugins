# PHP-FPM Check

# Overview

The PHP-FPM check monitors the state of your FPM pool and tracks request performance.

# Installation

The PHP-FPM check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=PHP-FPM). To install the PHP-FPM check install the `sd-agent-php_fpm` package.

# Configuration

Create a file `php_fpm.yaml` in the Agent's `conf.d` directory:

```
init_config:

instances:
  - status_url: http://localhost/status # or whatever pm.status_path is set to in your PHP INI
    ping_url: http://localhost/ping     # or whatever ping.path is set to in your PHP INI
    ping_reply: pong                    # the reply to expect from ping; default is 'pong'
#   user: <YOUR_USERNAME>     # if the status and ping URLs require HTTP basic auth
#   password: <YOUR_PASSWORD> # if the status and ping URLs require HTTP basic auth
#   http_host: <HOST>         # if your FPM pool is only accessible via a specific HTTP vhost
#   tags:
#     - instance:foo
```

Restart the Agent to start sending PHP-FPM metrics to Server Density.

# Validation

Run the Agent's `info` subcommand and look for `php_fpm` under the Checks section:

```
  Checks
  ======
    [...]

    php_fpm
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Compatibility

The php_fpm check is compatible with all major platforms.

# Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this check.

