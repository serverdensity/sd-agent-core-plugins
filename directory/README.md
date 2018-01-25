# Directory Check

## Overview

Capture metrics from directories and files of your choosing. The Agent will collect:

  * number of files
  * file size
  * age of the last modification
  * age of the creation

## Setup
### Installation

The Directory check can be installed with your package manager, if the sd-agent repository is configured on your server, [instructions are available on our support site](https://support.serverdensity.com/hc/en-us/search?query=directory). To install the directory check install the `sd-agent-directory` package.

### Configuration

1. Edit your `directory.yaml` file in the Agent's `conf.d` directory. See the [sample directory.yaml](https://github.com/serverdensity/sd-agent-core-plugins/blob/master/directory/conf.yaml.example) for all available configuration options:

```
init_config:

instances:
  - directory: "/path/to/directory" # the only required option
    name: "my_monitored_dir"        # What the Agent will tag this directory's metrics with. Defaults to "directory"
    pattern: "*.log"                # defaults to "*" (all files)
    recursive: True                 # default False
    countonly: False                # set to True to only collect the number of files matching 'pattern'. Useful for very large directories.
```

Ensure that the user running the Agent process (usually `sd-agent`) has read access to the directories, subdirectories, and files you configure.

2. Restart the Agent to begin sending metrics on your chosen directories to Server Density.

### Validation

Run the Agent's `info` subcommand and look for `directory` under the Checks section:

```
  Checks
  ======
    [...]

    directory
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The directory check is compatible with all major platforms.

## Data Collected
### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

