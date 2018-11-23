# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import requests
from prometheus_client.parser import text_string_to_metric_families
from six import iteritems, string_types
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from checks import AgentCheck


METRIC_MAP = {
    'addsstable_applications': 'addsstable.applications',
    'addsstable_copies': 'addsstable.copies',
    'addsstable_proposals': 'addsstable.proposals',
    'build_timestamp': 'build.timestamp',
    'capacity': 'capacity.total',
    'capacity_available': 'capacity.available',
    'capacity_reserved': 'capacity.reserved',
    'capacity_used': 'capacity.used',
    'clock_offset_meannanos': 'clock.offset.meannanos',
    'clock_offset_stddevnanos': 'clock.offset.stddevnanos',
    'compactor_compactingnanos': 'compactor.compactingnanos',
    'compactor_compactions_failure': 'compactor.compactions.failure',
    'compactor_compactions_success': 'compactor.compactions.success',
    'compactor_suggestionbytes_compacted': 'compactor.suggestionbytes.compacted',
    'compactor_suggestionbytes_queued': 'compactor.suggestionbytes.queued',
    'compactor_suggestionbytes_skipped': 'compactor.suggestionbytes.skipped',
    'distsender_batches_partial': 'distsender.batches.partial',
    'distsender_batches': 'distsender.batches.total',
    'distsender_errors_notleaseholder': 'distsender.errors.notleaseholder',
    'distsender_rpc_sent_local': 'distsender.rpc.sent.local',
    'distsender_rpc_sent_nextreplicaerror': 'distsender.rpc.sent.nextreplicaerror',
    'distsender_rpc_sent': 'distsender.rpc.sent.total',
    'exec_error': 'exec.error',
    'exec_latency': 'exec.latency',
    'exec_success': 'exec.success',
    'gcbytesage': 'gcbytesage',
    'gossip_bytes_received': 'gossip.bytes.received',
    'gossip_bytes_sent': 'gossip.bytes.sent',
    'gossip_connections_incoming': 'gossip.connections.incoming',
    'gossip_connections_outgoing': 'gossip.connections.outgoing',
    'gossip_connections_refused': 'gossip.connections.refused',
    'gossip_infos_received': 'gossip.infos.received',
    'gossip_infos_sent': 'gossip.infos.sent',
    'intentage': 'intentage',
    'intentbytes': 'intentbytes',
    'intentcount': 'intentcount',
    'keybytes': 'keybytes',
    'keycount': 'keycount',
    'lastupdatenanos': 'lastupdatenanos',
    'leases_epoch': 'leases.epoch',
    'leases_error': 'leases.error',
    'leases_expiration': 'leases.expiration',
    'leases_success': 'leases.success',
    'leases_transfers_error': 'leases.transfers.error',
    'leases_transfers_success': 'leases.transfers.success',
    'livebytes': 'livebytes',
    'livecount': 'livecount',
    'liveness_epochincrements': 'liveness.epochincrements',
    'liveness_heartbeatfailures': 'liveness.heartbeatfailures',
    'liveness_heartbeatlatency': 'liveness.heartbeatlatency',
    'liveness_heartbeatsuccesses': 'liveness.heartbeatsuccesses',
    'liveness_livenodes': 'liveness.livenodes',
    'node_id': 'node_id',
    'queue_consistency_pending': 'queue.consistency.pending',
    'queue_consistency_process_failure': 'queue.consistency.process.failure',
    'queue_consistency_process_success': 'queue.consistency.process.success',
    'queue_consistency_processingnanos': 'queue.consistency.processingnanos',
    'queue_gc_info_abortspanconsidered': 'queue.gc.info.abortspanconsidered',
    'queue_gc_info_abortspangcnum': 'queue.gc.info.abortspangcnum',
    'queue_gc_info_abortspanscanned': 'queue.gc.info.abortspanscanned',
    'queue_gc_info_intentsconsidered': 'queue.gc.info.intentsconsidered',
    'queue_gc_info_intenttxns': 'queue.gc.info.intenttxns',
    'queue_gc_info_numkeysaffected': 'queue.gc.info.numkeysaffected',
    'queue_gc_info_pushtxn': 'queue.gc.info.pushtxn',
    'queue_gc_info_resolvesuccess': 'queue.gc.info.resolvesuccess',
    'queue_gc_info_resolvetotal': 'queue.gc.info.resolvetotal',
    'queue_gc_info_transactionspangcaborted': 'queue.gc.info.transactionspangcaborted',
    'queue_gc_info_transactionspangccommitted': 'queue.gc.info.transactionspangccommitted',
    'queue_gc_info_transactionspangcpending': 'queue.gc.info.transactionspangcpending',
    'queue_gc_info_transactionspanscanned': 'queue.gc.info.transactionspanscanned',
    'queue_gc_pending': 'queue.gc.pending',
    'queue_gc_process_failure': 'queue.gc.process.failure',
    'queue_gc_process_success': 'queue.gc.process.success',
    'queue_gc_processingnanos': 'queue.gc.processingnanos',
    'queue_raftlog_pending': 'queue.raftlog.pending',
    'queue_raftlog_process_failure': 'queue.raftlog.process.failure',
    'queue_raftlog_process_success': 'queue.raftlog.process.success',
    'queue_raftlog_processingnanos': 'queue.raftlog.processingnanos',
    'queue_raftsnapshot_pending': 'queue.raftsnapshot.pending',
    'queue_raftsnapshot_process_failure': 'queue.raftsnapshot.process.failure',
    'queue_raftsnapshot_process_success': 'queue.raftsnapshot.process.success',
    'queue_raftsnapshot_processingnanos': 'queue.raftsnapshot.processingnanos',
    'queue_replicagc_pending': 'queue.replicagc.pending',
    'queue_replicagc_process_failure': 'queue.replicagc.process.failure',
    'queue_replicagc_process_success': 'queue.replicagc.process.success',
    'queue_replicagc_processingnanos': 'queue.replicagc.processingnanos',
    'queue_replicagc_removereplica': 'queue.replicagc.removereplica',
    'queue_replicate_addreplica': 'queue.replicate.addreplica',
    'queue_replicate_pending': 'queue.replicate.pending',
    'queue_replicate_process_failure': 'queue.replicate.process.failure',
    'queue_replicate_process_success': 'queue.replicate.process.success',
    'queue_replicate_processingnanos': 'queue.replicate.processingnanos',
    'queue_replicate_purgatory': 'queue.replicate.purgatory',
    'queue_replicate_rebalancereplica': 'queue.replicate.rebalancereplica',
    'queue_replicate_removedeadreplica': 'queue.replicate.removedeadreplica',
    'queue_replicate_removereplica': 'queue.replicate.removereplica',
    'queue_replicate_transferlease': 'queue.replicate.transferlease',
    'queue_split_pending': 'queue.split.pending',
    'queue_split_process_failure': 'queue.split.process.failure',
    'queue_split_process_success': 'queue.split.process.success',
    'queue_split_processingnanos': 'queue.split.processingnanos',
    'queue_tsmaintenance_pending': 'queue.tsmaintenance.pending',
    'queue_tsmaintenance_process_failure': 'queue.tsmaintenance.process.failure',
    'queue_tsmaintenance_process_success': 'queue.tsmaintenance.process.success',
    'queue_tsmaintenance_processingnanos': 'queue.tsmaintenance.processingnanos',
    'raft_commandsapplied': 'raft.commandsapplied',
    'raft_enqueued_pending': 'raft.enqueued.pending',
    'raft_heartbeats_pending': 'raft.heartbeats.pending',
    'raft_process_commandcommit_latency': 'raft.process.commandcommit.latency',
    'raft_process_logcommit_latency': 'raft.process.logcommit.latency',
    'raft_process_tickingnanos': 'raft.process.tickingnanos',
    'raft_process_workingnanos': 'raft.process.workingnanos',
    'raft_rcvd_app': 'raft.rcvd.app',
    'raft_rcvd_appresp': 'raft.rcvd.appresp',
    'raft_rcvd_dropped': 'raft.rcvd.dropped',
    'raft_rcvd_heartbeat': 'raft.rcvd.heartbeat',
    'raft_rcvd_heartbeatresp': 'raft.rcvd.heartbeatresp',
    'raft_rcvd_prevote': 'raft.rcvd.prevote',
    'raft_rcvd_prevoteresp': 'raft.rcvd.prevoteresp',
    'raft_rcvd_prop': 'raft.rcvd.prop',
    'raft_rcvd_snap': 'raft.rcvd.snap',
    'raft_rcvd_timeoutnow': 'raft.rcvd.timeoutnow',
    'raft_rcvd_transferleader': 'raft.rcvd.transferleader',
    'raft_rcvd_vote': 'raft.rcvd.vote',
    'raft_rcvd_voteresp': 'raft.rcvd.voteresp',
    'raft_ticks': 'raft.ticks',
    'raftlog_behind': 'raftlog.behind',
    'raftlog_truncated': 'raftlog.truncated',
    'range_adds': 'range.adds',
    'range_raftleadertransfers': 'range.raftleadertransfers',
    'range_removes': 'range.removes',
    'range_snapshots_generated': 'range.snapshots.generated',
    'range_snapshots_normal_applied': 'range.snapshots.normal_applied',
    'range_snapshots_preemptive_applied': 'range.snapshots.preemptive_applied',
    'range_splits': 'range.splits.total',
    'ranges': 'ranges',
    'ranges_unavailable': 'ranges.unavailable',
    'ranges_underreplicated': 'ranges.underreplicated',
    'rebalancing_writespersecond': 'rebalancing.writespersecond',
    'replicas_commandqueue_combinedqueuesize': 'replicas.commandqueue.combinedqueuesize',
    'replicas_commandqueue_combinedreadcount': 'replicas.commandqueue.combinedreadcount',
    'replicas_commandqueue_combinedwritecount': 'replicas.commandqueue.combinedwritecount',
    'replicas_commandqueue_maxoverlaps': 'replicas.commandqueue.maxoverlaps',
    'replicas_commandqueue_maxreadcount': 'replicas.commandqueue.maxreadcount',
    'replicas_commandqueue_maxsize': 'replicas.commandqueue.maxsize',
    'replicas_commandqueue_maxtreesize': 'replicas.commandqueue.maxtreesize',
    'replicas_commandqueue_maxwritecount': 'replicas.commandqueue.maxwritecount',
    'replicas_leaders': 'replicas.leaders',
    'replicas_leaders_not_leaseholders': 'replicas.leaders.not_leaseholders',
    'replicas_leaseholders': 'replicas.leaseholders',
    'replicas_quiescent': 'replicas.quiescent',
    'replicas_reserved': 'replicas.reserved',
    'replicas': 'replicas.total',
    'requests_backpressure_split': 'requests.backpressure.split',
    'requests_slow_commandqueue': 'requests.slow.commandqueue',
    'requests_slow_distsender': 'requests.slow.distsender',
    'requests_slow_lease': 'requests.slow.lease',
    'requests_slow_raft': 'requests.slow.raft',
    'rocksdb_block_cache_hits': 'rocksdb.block.cache.hits',
    'rocksdb_block_cache_misses': 'rocksdb.block.cache.misses',
    'rocksdb_block_cache_pinned_usage': 'rocksdb.block.cache.pinned.usage',
    'rocksdb_block_cache_usage': 'rocksdb.block.cache.usage',
    'rocksdb_bloom_filter_prefix_checked': 'rocksdb.bloom_filter.prefix.checked',
    'rocksdb_bloom_filter_prefix_useful': 'rocksdb.bloom_filter.prefix.useful',
    'rocksdb_compactions': 'rocksdb.compactions.total',
    'rocksdb_flushes': 'rocksdb.flushes.total',
    'rocksdb_memtable_total_size': 'rocksdb.memtable.total.size',
    'rocksdb_num_sstables': 'rocksdb.num_sstables',
    'rocksdb_read_amplification': 'rocksdb.read.amplification',
    'rocksdb_table_readers_mem_estimate': 'rocksdb.table.readers.mem.estimate',
    'round_trip_latency': 'round_trip.latency',
    'sql_bytesin': 'sql.bytesin',
    'sql_bytesout': 'sql.bytesout',
    'sql_conns': 'sql.conns',
    'sql_ddl_count': 'sql.ddl.count',
    'sql_delete_count': 'sql.delete.count',
    'sql_distsql_exec_latency': 'sql.distsql.exec.latency',
    'sql_distsql_flows_active': 'sql.distsql.flows.active',
    'sql_distsql_flows_total': 'sql.distsql.flows.total',
    'sql_distsql_queries_active': 'sql.distsql.queries.active',
    'sql_distsql_queries_total': 'sql.distsql.queries.total',
    'sql_distsql_select_count': 'sql.distsql.select.count',
    'sql_distsql_service_latency': 'sql.distsql.service.latency',
    'sql_exec_latency': 'sql.exec.latency',
    'sql_insert_count': 'sql.insert.count',
    'sql_mem_admin_current': 'sql.mem.admin.current',
    'sql_mem_admin_max': 'sql.mem.admin.max',
    'sql_mem_admin_session_current': 'sql.mem.admin.session.current',
    'sql_mem_admin_session_max': 'sql.mem.admin.session.max',
    'sql_mem_admin_txn_current': 'sql.mem.admin.txn.current',
    'sql_mem_admin_txn_max': 'sql.mem.admin.txn.max',
    'sql_mem_client_current': 'sql.mem.client.current',
    'sql_mem_client_max': 'sql.mem.client.max',
    'sql_mem_client_session_current': 'sql.mem.client.session.current',
    'sql_mem_client_session_max': 'sql.mem.client.session.max',
    'sql_mem_client_txn_current': 'sql.mem.client.txn.current',
    'sql_mem_client_txn_max': 'sql.mem.client.txn.max',
    'sql_mem_conns_current': 'sql.mem.conns.current',
    'sql_mem_conns_max': 'sql.mem.conns.max',
    'sql_mem_conns_session_current': 'sql.mem.conns.session.current',
    'sql_mem_conns_session_max': 'sql.mem.conns.session.max',
    'sql_mem_conns_txn_current': 'sql.mem.conns.txn.current',
    'sql_mem_conns_txn_max': 'sql.mem.conns.txn.max',
    'sql_mem_distsql_current': 'sql.mem.distsql.current',
    'sql_mem_distsql_max': 'sql.mem.distsql.max',
    'sql_mem_internal_current': 'sql.mem.internal.current',
    'sql_mem_internal_max': 'sql.mem.internal.max',
    'sql_mem_internal_session_current': 'sql.mem.internal.session.current',
    'sql_mem_internal_session_max': 'sql.mem.internal.session.max',
    'sql_mem_internal_txn_current': 'sql.mem.internal.txn.current',
    'sql_mem_internal_txn_max': 'sql.mem.internal.txn.max',
    'sql_misc_count': 'sql.misc.count',
    'sql_query_count': 'sql.query.count',
    'sql_select_count': 'sql.select.count',
    'sql_service_latency': 'sql.service.latency',
    'sql_txn_abort_count': 'sql.txn.abort.count',
    'sql_txn_begin_count': 'sql.txn.begin.count',
    'sql_txn_commit_count': 'sql.txn.commit.count',
    'sql_txn_rollback_count': 'sql.txn.rollback.count',
    'sql_update_count': 'sql.update.count',
    'sys_cgo_allocbytes': 'sys.cgo.allocbytes',
    'sys_cgo_totalbytes': 'sys.cgo.totalbytes',
    'sys_cgocalls': 'sys.cgocalls',
    'sys_cpu_sys_ns': 'sys.cpu.sys.ns',
    'sys_cpu_sys_percent': 'sys.cpu.sys.percent',
    'sys_cpu_user_ns': 'sys.cpu.user.ns',
    'sys_cpu_user_percent': 'sys.cpu.user.percent',
    'sys_fd_open': 'sys.fd.open',
    'sys_fd_softlimit': 'sys.fd.softlimit',
    'sys_gc_count': 'sys.gc.count',
    'sys_gc_pause_ns': 'sys.gc.pause.ns',
    'sys_gc_pause_percent': 'sys.gc.pause.percent',
    'sys_go_allocbytes': 'sys.go.allocbytes',
    'sys_go_totalbytes': 'sys.go.totalbytes',
    'sys_goroutines': 'sys.goroutines',
    'sys_rss': 'sys.rss',
    'sys_uptime': 'sys.uptime',
    'sysbytes': 'sysbytes',
    'syscount': 'syscount',
    'timeseries_write_bytes': 'timeseries.write.bytes',
    'timeseries_write_errors': 'timeseries.write.errors',
    'timeseries_write_samples': 'timeseries.write.samples',
    'totalbytes': 'totalbytes',
    'tscache_skl_read_pages': 'tscache.skl.read.pages',
    'tscache_skl_read_rotations': 'tscache.skl.read.rotations',
    'tscache_skl_write_pages': 'tscache.skl.write.pages',
    'tscache_skl_write_rotations': 'tscache.skl.write.rotations',
    'txn_abandons': 'txn.abandons',
    'txn_aborts': 'txn.aborts',
    'txn_autoretries': 'txn.autoretries',
    'txn_commits': 'txn.commits',
    'txn_commits1PC': 'txn.commits1PC',
    'txn_durations': 'txn.durations',
    'txn_restarts': 'txn.restarts',
    'txn_restarts_deleterange': 'txn.restarts.deleterange',
    'txn_restarts_possiblereplay': 'txn.restarts.possiblereplay',
    'txn_restarts_serializable': 'txn.restarts.serializable',
    'txn_restarts_writetooold': 'txn.restarts.writetooold',
    'valbytes': 'valbytes',
    'valcount': 'valcount',
}

class CockroachDB(AgentCheck):
    def check(self, instance):
        config = {}
        config['send_monotonic_counter'] = instance.get('send_monotonic_counter', True)
        config['send_histograms_buckets'] = instance.get('send_histograms_buckets', False)
        config['rename_le'] = instance.get('rename_le_label', True)
        config['prometheus_url'] = instance.get('prometheus_url', 'http://localhost:8080/_status/vars')
        config['timeout'] = float(instance.get('prometheus_timeout', 10))
        config['ssl_cert'] = instance.get('ssl_cert', None)
        config['ssl_private_key'] = instance.get('ssl_private_key', None)
        config['ssl_ca_cert'] = instance.get('ssl_ca_cert', None)
        cert = None
        if isinstance(config['ssl_cert'], string_types):
            if isinstance(config['ssl_private_key'], string_types):
                cert = (config['ssl_cert'], config['ssl_private_key'])
            else:
                cert = config['ssl_cert']

        verify = True
        if config['ssl_ca_cert'] is False:
            verify = False

        if isinstance(config['ssl_ca_cert'], string_types):
            verify = config['ssl_ca_cert']
        elif verify is False:
            disable_warnings(InsecureRequestWarning)
        try:
            r = requests.get("{}".format(config['prometheus_url']), timeout=config['timeout'], cert=cert, verify=verify)
            for metric in text_string_to_metric_families(r.content):
                try:
                    metric_name = 'cockroachdb.{}'.format(METRIC_MAP[metric.name])
                except KeyError:
                    metric_name = 'cockroachdb.{}'.format(metric.name.replace('_','.'))
                if metric.type in ["gauge", "counter", "rate"]:
                    for sample in metric.samples:
                        tags = []
                        tags = self._metric_tags(sample,config,tags,instance)
                        if metric.type == "counter" and config['send_monotonic_counter']:
                            self.monotonic_count(metric_name, float(sample[2]), tags=tags)
                        elif metric.type == "rate":
                            self.rate(metric_name, float(sample[2]), tags=tags)
                        else:
                            self.gauge(metric_name, float(sample[2]), tags=tags)
                elif metric.type == "histogram":
                    for sample in metric.samples:
                        tags = []
                        tags = self._metric_tags(sample,config,tags,instance)
                        val = sample[2]
                        if sample[0].endswith("_sum"):
                            self.gauge("{}.sum".format(metric_name), val, tags=tags)
                        elif sample[0].endswith("_count"):
                            self.gauge("{}.count".format(metric_name), val, tags=tags)
                        elif (config['send_histograms_buckets'] and sample[0].endswith("_bucket") and
                                "Inf" not in sample[1]["le"]):
                            sample[1]["le"] = float(sample[1]["le"])
                            self.gauge("{}.count".format(metric_name), val, tags=tags)
        except Exception as e:
            self.log.exception("Failed to collect cockroachdb metrics: ".format(e))


    def _metric_tags(self,sample,config,tags,instance):
        tags = list(instance.get('tags', []))
        if config['prometheus_url']:
            tags.extend(['server:{}'.format(config['prometheus_url'])])
        for label_name, label_value in iteritems(sample[1]):
            if label_name == "le" and config['rename_le']:
                label_name = "upper_bound"
                label_value = float(label_value)
            elif label_name == "le" and not config['rename_le']:
                label_value = float(label_value)
            tags.extend(['{}:{}'.format(label_name, label_value)])
        return tags

if __name__ == '__main__':
    # Load the check and instance configurations
    check, instances = CockroachDB.from_yaml('/etc/sd-agent/conf.d/cockroachdb.yaml')
    for instance in instances:
        print "\nRunning the check against host: {}:{}".format(instance.get('prometheus_url','http://localhost:8080/_status/vars'))
        check.check(instance)
        print 'Metrics: {}'.format(check.get_metrics())
