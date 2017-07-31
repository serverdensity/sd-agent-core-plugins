# Cacti Integration

# Overview

Get metrics from cacti service in real time to:

* Visualize and monitor cacti states
* Be notified about cacti failovers and events.

# Installation

The Cacti check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=cacti). To install the cacti check install the `sd-agent-cacti` package.

# Configuration

Create a serverdensity user with read-only rights to the Cacti database

```
sudo mysql -e "create user 'serverdensity'@'localhost' identified by '<password>';"
sudo mysql -e "grant select on cacti.* to 'serverdensity'@'localhost';"
```

Check user and rights

```
mysql -u serverdensity --password=<password> -e "show status" | \
grep Uptime && echo -e "\033[0;32mMySQL user - OK\033[0m" || \
echo -e "\033[0;31mCannot connect to MySQL\033[0m"

mysql -u serverdensity --password=<password> -D cacti -e "select * from data_template_data limit 1" && \
echo -e "\033[0;32mMySQL grant - OK\033[0m" || \
echo -e "\033[0;31mMissing SELECT grant\033[0m"
```

Configure the Agent to connect to MySQL
Edit conf.d/cacti.yaml

```
init_config:

instances:
    -   mysql_host: localhost
        mysql_user: serverdensity
        mysql_password: hx3beOpMFcvxn9gXcs0MU3jX
        rrd_path: /path/to/cacti/rra
        #field_names:
        #    - ifName
        #    - dskDevice
        #    - ifIndex
        #rrd_whitelist: /path/to/rrd_whitelist.txt
```

Give the sd-agent user access to the RRD files

```
sudo gpasswd -a sd-agent www-data
sudo chmod -R g+rx /var/lib/cacti/rra/
sudo su - sd-agent -c 'if [ -r /var/lib/cacti/rra/ ];
then echo -e "\033[0;31msd-agent can read the RRD files\033[0m";
else echo -e "\033[0;31msd-agent can not read the RRD files\033[0m";
fi'
```

# Validation

Run the Agent's `info` subcommand and look for `cacti` under the Checks section:

```
  Checks
  ======
    [...]

    cacti
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

# Troubleshooting

# Compatibility

The cacti check is compatible with all major platforms

# Metrics
