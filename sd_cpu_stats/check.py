import re

# project
import string
import subprocess
import sys
from checks import AgentCheck
from utils.subprocess_output import get_subprocess_output


class ServerDensityCPUChecks(AgentCheck):
    """Collects metrics about the machine's CPU cores."""

    def check(self, instance):

        def get_value(legend, data, name, filter_value=None):
            "Using the legend and a metric name, get the value or None from the data line"
            if name in legend:
                value = data[legend.index(name)]
                if filter_value is not None:
                    if value > filter_value:
                        return None
                return value

            else:
                # FIXME return a float or False, would trigger type error if not python
                self.log.debug("Cannot extract cpu value %s from %s (%s)" % (name, data, legend))
                return 0.0

        self.log.debug('getCPUStats: start')

        cpu_stats = {}
        if 'linux' in sys.platform:
            self.log.debug('getCPUStats: linux')

            headerRegexp = re.compile(r'.*?([%][a-zA-Z0-9]+)[\s+]?')
            itemRegexp = re.compile(r'.*?\s+(\d+)[\s+]?')
            valueRegexp = re.compile(r'\d+\.\d+')
            proc = None
            try:
                proc = subprocess.Popen(['mpstat', '-P', 'ALL', '1', '1'], stdout=subprocess.PIPE, close_fds=True)
                stats = proc.communicate()[0]

                try:
                    proc.kill()
                except Exception:
                    self.log.debug('Process already terminated')

                stats = stats.decode('utf-8').split('\n')
                header = stats[2]
                headerNames = re.findall(headerRegexp, header)
                device = None

                for statsIndex in range(3, len(stats)):
                    row = stats[statsIndex]

                    if not row:  # skip the averages
                        break

                    deviceMatch = re.match(itemRegexp, row)

                    if str.find(row, 'all') is not -1:
                        device = 'ALL'
                    elif deviceMatch is not None:
                        device = 'CPU%s' % deviceMatch.groups()[0]

                    values = re.findall(valueRegexp, row.replace(',', '.'))

                    cpu_stats[device] = {}
                    for headerIndex in range(0, len(headerNames)):
                        headerName = headerNames[headerIndex]
                        cpu_stats[device][headerName] = values[headerIndex]
                        key = headerName.replace('%', '')
                        self.gauge('serverdensity.cpu.{0}'.format(key), float(values[headerIndex]), device_name=device)

            except OSError:
                # we dont have it installed return nothing
                return

            except Exception:
                import traceback
                self.log.error("getCPUStats: exception = %s", traceback.format_exc())

                try:
                    if proc is not None:
                        proc.kill()
                except UnboundLocalError:
                    self.log.debug('Process already terminated')
                except Exception:
                    self.log.debug('Process already terminated')
                return

        elif sys.platform == 'darwin':
            self.log.debug('getCPUStats: darwin')

            try:
                # generate 3 seconds of data
                # ['          disk0           disk1       cpu     load average', '    KB/t tps  MB/s     KB/t tps  MB/s  us sy id   1m   5m   15m', '   21.23  13  0.27    17.85   7  0.13  14  7 79  1.04 1.27 1.31', '    4.00   3  0.01     5.00   8  0.04  12 10 78  1.04 1.27 1.31', '']
                iostats, _, _ = get_subprocess_output(['iostat', '-C', '-w', '3', '-c', '2'], self.log)
                lines = [l for l in iostats.splitlines() if len(l) > 0]
                legend = [l for l in lines if "us" in l]
                if len(legend) == 1:
                    headers = legend[0].split()
                    data = lines[-1].split()
                    self.gauge('serverdensity.cpu.usr', float(get_value(headers, data, "us")), device_name='ALL')
                    self.gauge('serverdensity.cpu.sys', float(get_value(headers, data, "sy")), device_name='ALL')
                    self.gauge('serverdensity.cpu.idle', float(get_value(headers, data, "id")), device_name='ALL')
                else:
                    self.logger.warn("Expected to get at least 4 lines of data from iostat instead of just " + str(iostats[:max(80, len(iostats))]))

            except Exception:
                import traceback
                self.log.error('getCPUStats: exception = %s', traceback.format_exc())
                return

        elif sys.platform.startswith("freebsd"):
            # generate 3 seconds of data
            # tty            ada0              cd0            pass0             cpu
            # tin  tout  KB/t tps  MB/s   KB/t tps  MB/s   KB/t tps  MB/s  us ni sy in id
            # 0    69 26.71   0  0.01   0.00   0  0.00   0.00   0  0.00   2  0  0  1 97
            # 0    78  0.00   0  0.00   0.00   0  0.00   0.00   0  0.00   0  0  0  0 100
            iostats, _, _ = get_subprocess_output(['iostat', '-w', '3', '-c', '2'], self.log)
            lines = [l for l in iostats.splitlines() if len(l) > 0]
            legend = [l for l in lines if "us" in l]
            if len(legend) == 1:
                headers = legend[0].split()
                data = lines[-1].split()
                cpu_user = get_value(headers, data, "us")
                cpu_nice = get_value(headers, data, "ni")
                cpu_sys = get_value(headers, data, "sy")
                cpu_intr = get_value(headers, data, "in")
                cpu_idle = get_value(headers, data, "id")
                self.gauge('serverdensity.cpu.usr', float(cpu_user), device_name='ALL')
                self.gauge('serverdensity.cpu.nice', float(cpu_nice), device_name='ALL')
                self.gauge('serverdensity.cpu.sys', float(cpu_sys), device_name='ALL')
                self.gauge('serverdensity.cpu.irq', float(cpu_intr), device_name='ALL')
                self.gauge('serverdensity.cpu.idle', float(cpu_idle), device_name='ALL')
                cpu_stats['ALL'] = {
                    'usr': cpu_user,
                    'nice': cpu_nice,
                    'sys': cpu_sys,
                    'irq': cpu_intr,
                    'idle': cpu_idle,
                }

            else:
                self.logger.warn("Expected to get at least 4 lines of data from iostat instead of just " + str(iostats[:max(80, len(iostats))]))
                return

        else:
            self.log.debug('getCPUStats: unsupported platform')
            return

        self.log.debug('getCPUStats: completed, returning')
