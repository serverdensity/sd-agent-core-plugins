# stdlib
from urlparse import urljoin

# 3rd party
import requests

# project
from checks import AgentCheck


class StormCheck(AgentCheck):
    '''Extract info from Storm REST api
    http://storm.apache.org/releases/0.10.1/STORM-UI-REST-API.html'''

    URL_PATHS = {
        'topology_summary': '/api/v1/topology/summary',
        'topology_info': '/api/v1/topology/{id}'
    }

    def check(self, instance):

        server = instance.get('server')
        if server is None:
            raise Exception('A server must be specified')

        topologies = self._get_topology_summary(server)

        for topology in topologies.get('topologies', []):
            topology_status = topology['status']
            topology_name = topology['name']
            topology_id = topology['id']

            if topology_status == 'ACTIVE':
                topology_tag = 'topology:{}'.format(topology_name)

                topology_info = self._get_topology_info(
                    server, topology_id)

                topology_stats = topology_info['topologyStats']
                topology_info_status = topology_info['status']

                if topology_info_status == 'ACTIVE':
                    topology_stats_10m_0s = topology_stats[0]
                    topology_stats_10m_0s_data = [
                        ('storm.topology.stats.complete_latency',
                         topology_stats_10m_0s['completeLatency']),
                        ('storm.topology.stats.acked',
                         topology_stats_10m_0s['acked']),
                        ('storm.topology.stats.failed',
                         topology_stats_10m_0s['failed']),
                    ]

                    for data in topology_stats_10m_0s_data:
                        metric, metric_value = data

                        self.gauge(metric, metric_value, tags=[topology_tag])

                    spouts = topology_info.get('spouts', [])

                    for spout in spouts:
                        spout_id = spout['spoutId']

                        spout_tag = 'spout:{}'.format(spout_id)

                        spout_data = [
                            ('storm.spouts.complete_latency',
                             spout['completeLatency']),
                            ('storm.spouts.failed', spout['failed'])
                        ]

                        for data in spout_data:
                            metric, metric_value = data

                            self.gauge(metric, metric_value, tags=[
                                       topology_tag, spout_tag])

                    bolts = topology_info.get('bolts', [])

                    for bolt in bolts:
                        bolt_id = bolt['boltId']

                        bolt_tag = 'bolt:{}'.format(bolt_id)

                        bolt_data = [
                            ('storm.bolts.execute_latency',
                             bolt['executeLatency']),
                            ('storm.bolts.process_latency',
                             bolt['processLatency']),
                            ('storm.bolts.failed', bolt['failed'])
                        ]

                        for data in bolt_data:
                            metric, metric_value = data

                            self.gauge(metric, metric_value, tags=[
                                       topology_tag, bolt_tag])

    def _get_data(self, url):
        return requests.get(url).json()

    def _get_topology_summary(self, server):
        url = urljoin(server, self.URL_PATHS['topology_summary'])

        return self._get_data(url)

    def _get_topology_info(self, server, id):
        url = urljoin(server, self.URL_PATHS['topology_info'].format(id=id))

        return self._get_data(url)


if __name__ == '__main__':
    pass
