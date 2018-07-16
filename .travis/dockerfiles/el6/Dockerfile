FROM centos:6
RUN yum -y install \
    yum-utils \
    rpm-build \
    redhat-rpm-config \
    make \
    gcc \
    wget \
    curl \
    libyaml-devel \
    curl-devel \
    tar \
    symlinks \
    epel-release
RUN wget https://centos6.iuscommunity.org/ius-release.rpm && \
    rpm -Uvh ius-release*.rpm && \
    yum -y install python27 python27-devel
RUN wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-centos96-9.6-3.noarch.rpm && \
    rpm -Uvh pg*.rpm && \
    yum -y install postgresql96-devel postgresql96-libs postgresql96
RUN ( grep -q :20: /etc/group || groupadd -g 20 osx_staff ) && \
    ( grep -q :501: /etc/passwd || useradd -u 501 -g 20 osx_user ) && \
    ( grep -q :1000: /etc/group || groupadd -g 1000 ubuntu_group ) && \
    ( grep -q :1000: /etc/passwd || useradd  -u 1000 -g 1000 ubuntu_user )
COPY ./entrypoint.sh /
ENV PATH "$PATH:/usr/pgsql-9.6/bin/"
CMD ["/entrypoint.sh"]
