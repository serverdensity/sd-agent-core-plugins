# SO references
# http://stackoverflow.com/questions/880227/what-is-the-minimum-i-have-to-do-to-create-an-rpm-file

# Init script references
# http://fedoraproject.org/wiki/Packaging/SysVInitScript#InitscriptScriptlets

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress
%global        __venv %{_tmppath}/venv
%global          longdescription %include description
%global        __sd_python_version 2.7

Summary: Server Density Monitoring Agent
Name: sd-agent
BuildArch: x86_64 i386
%include %{_topdir}/inc/version
%include %{_topdir}/inc/release
Requires: python >= 2.7, sysstat, libyaml
BuildRequires: symlinks, libffi-devel, python27-devel, openssl-devel, rrdtool-devel, postgresql-devel  >= 9.1, postgresql-libs >= 9.1
License: Simplified BSD
Group: System/Monitoring
Source: sd-agent-core-plugins-%{version}.tar.gz
URL: http://www.serverdensity.com/


BuildRoot: %{_tmppath}/sd-agent-core-plugins-%{version}-%{release}-root

%description
%{longdescription}

%prep
curl -LO https://raw.github.com/pypa/virtualenv/1.11.6/virtualenv.py
python2.7 virtualenv.py --no-site-packages --no-pip --no-setuptools %{__venv}
curl -LO https://bootstrap.pypa.io/ez_setup.py
%{__venv}/bin/python ez_setup.py --version="20.9.0"
curl -LO https://bootstrap.pypa.io/get-pip.py
%{__venv}/bin/python get-pip.py

%setup -qn sd-agent-core-plugins
for plugin in activemq_xml agent_metrics apache btrfs cacti cassandra ceph cockroachdb consul couch couchbase directory disk dns_check docker_daemon elastic entropy etcd fluentd gearmand gitlab gitlab_runner go_expvar go-metro gunicorn haproxy hdfs_datanode hdfs_namenode http_check jenkins kafka kafka_consumer kong kube_dns kubernetes kubernetes_state kyototycoon lighttpd linux_proc_extras mapreduce marathon mcache mdadm mesos_master mesos_slave mongo mysql network nfsstat nginx ntp openstack oracle pgbouncer php_fpm postfix postgres powerdns_recursor process rabbitmq redisdb riak riakcs snmp solr spark ssh_check statsd storm supervisord system_core system_swap tcp_check tokumx tomcat twemproxy varnish vsphere yarn zk; do
    echo ${plugin}
    %{__venv}/bin/python %{__venv}/bin/pip install --no-binary=:all: -r ${plugin}/requirements.txt
done

%build
%include %{_topdir}/pgbouncer-centos7
%include %{_topdir}/inc/install

%clean
rm -rf %{buildroot}

%post
/etc/init.d/sd-agent restart

%include %{_topdir}/inc/files
%include %{_topdir}/inc/subpackages
%include %{_topdir}/inc/changelog
