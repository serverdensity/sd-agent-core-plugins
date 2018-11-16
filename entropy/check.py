# (C) Server Density <hello@serverdensity.com> 2018
# (C) Vincent Lours <vl@ipggroup.com> 2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# agent
from checks import AgentCheck
from utils.platform import Platform
from utils.subprocess_output import get_subprocess_output


class Entropy(AgentCheck):
    def check(self, instance):
        #Check the status of Entropy
        if Platform.is_unix():
            try:
                data, _, _ = get_subprocess_output(
                    ['sudo', 'cat', '/proc/sys/kernel/random/entropy_avail'],
                    self.log, False)
                self.log.debug("Entropy Available:",str(data))
                self.gauge('system.entropy.available', int(data))
            except Exception as e:
                self.log.exception("Failed to collect entropy: ".format(e))
        else:
            self.log.warning(
                'Plugin currently only available on Linux.')
