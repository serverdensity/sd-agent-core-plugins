# CHANGELOG - elastic

1.3.0 / Unreleased
==================

### Changes

* [FEATURE] adds `pshard_graceful_timeout` that will skip pshard_stats if TO. See [#463][]
* [IMPROVEMENT] get rid of pretty json. See [#893][].

1.2.0 / 2017-11-21
==================
### Changes

* [UPDATE] Update auto_conf template to support agent 6 and 5.20+. See [#860][]

1.1.0 / 2017-11-21
==================

### Changes

* [BUG] Fixes bug for retreiving indices count. See [#806][]
* [FEATURE] Added more JVM metrics. See [#695][]
* [FEATURE] Add metric on the average time spent by tasks in the pending queue. See[#820][]

1.0.1 / 2017-08-28
==================

### Changes

* [FEATURE] Add metric for index count. See [#617][]

1.0.0 / 2017-03-22
==================

### Changes

* [FEATURE] adds elastic integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[#463]: https://github.com/DataDog/integrations-core/issues/463
[#617]: https://github.com/DataDog/integrations-core/issues/617
[#695]: https://github.com/DataDog/integrations-core/issues/695
[#806]: https://github.com/DataDog/integrations-core/issues/806
[#820]: https://github.com/DataDog/integrations-core/issues/820
[#860]: https://github.com/DataDog/integrations-core/issues/860
[#893]: https://github.com/DataDog/integrations-core/issues/893