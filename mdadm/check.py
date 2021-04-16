"""
  Server Density Plugin
  Mdadm Check
  Version: 1.1.0
"""

import json
import logging
import platform
import sys
import subprocess
import time

from checks import AgentCheck


class Mdadm(AgentCheck):
    """
    Collect mdadm device and disk metrics using output from
    /proc/mdstat via mdstat https://pypi.python.org/pypi/mdstat/
    """
    def check(self, instance):

        try:
            import mdstat
        except ImportError:
            self.log.error(
                "Could not import mdstat. \
                You will need to install mdstat in the sd-agent venv via pip: \
                /usr/share/python/sd-agent/bin/pip install mdstat")

        try:
            data = mdstat.parse()
            self.log.debug('mdstat.parse returned: {}'.format(data))
            self.gauge("system.mdadm.unused_devices",
                       len(data['unused_devices']))
            self.gauge("system.mdadm.in_use_devices",
                       len(data['devices']))
            for device in data['devices']:
                tags = []
                try:
                    tags.append("device:{}".format(device))
                    status_dict = data['devices'][device]['status']
                    if status_dict.get('raid_disks'):
                        # These keys are not present for RAID0 devices
                        degraded = status_dict['raid_disks'] != \
                            status_dict['non_degraded_disks']
                        self.gauge("system.mdadm.degraded",
                                   int(degraded), tags)
                    self.gauge("system.mdadm.read_only",
                               int(data['devices'][device]['read_only']), tags)
                    self.gauge("system.mdadm.active",
                               int(data['devices'][device]['active']), tags)
                    for metric in status_dict.keys():
                        if unicode(status_dict[metric]).isnumeric():
                            self.gauge("system.mdadm.{}".format(metric),
                                       status_dict[metric], tags)
                except Exception as e:
                    self.log.error(
                        'Error parsing {} device status: {}'.format(device, e),
                        exc_info=True)
                    continue
                try:
                    disks_dict = data['devices'][device]['disks']
                    for disk, metrics in disks_dict.iteritems():
                        disk_tags = []
                        disk_tags.append("disk:{}".format(disk))
                        disk_tags.extend(tags)
                        for metric, value in metrics.iteritems():
                            self.gauge("system.mdadm.disk.{}".format(metric),
                                       int(disks_dict[disk][metric]),
                                       disk_tags)
                except Exception as e:
                    self.log.error(
                        'Error parsing disk status: {}'.format(e),
                        exc_info=True)
                    continue

        except OSError as exception:
            self.checks_logger.error(
                'Unable to find mdstat.'
                ' Error: {0}'.format(exception.message))


if __name__ == '__main__':
    # Load the check and instance configurations
    check, instances = Mdadm.from_yaml('/etc/sd-agent/conf.d/mdadm.yaml')
    for instance in instances:
        print "\nRunning the mdadm check against host"
        check.check(instance)
        print 'Metrics: {}'.format(check.get_metrics())
