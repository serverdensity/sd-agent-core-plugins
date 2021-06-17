#!/bin/bash

DEBIAN_PATH="/sd-agent/debian"
UBUNTU=(bionic focal xenial trusty)

if [[ ${UBUNTU[*]} =~ ${RELEASE} ]]
then
    DISTRO="ubuntu"
else
    DISTRO="debian"
fi

sudo cp -a ${DEBIAN_PATH}/distros/${RELEASE}/. ${DEBIAN_PATH}
sudo sed -i "s|trusty|$RELEASE|" ${DEBIAN_PATH}/changelog
sudo dpkg-source -b /sd-agent

for ARCH in amd64 arm64; do
    if [ ! -d /packages/${DISTRO}/${RELEASE} ]; then
        sudo mkdir /packages/${DISTRO}/${RELEASE}
    fi
    if [ ! -d /packages/${DISTRO}/${RELEASE}/${ARCH} ]; then
        sudo mkdir /packages/${DISTRO}/${RELEASE}/${ARCH}
    fi
    pbuilder-dist $RELEASE $arch update
    pbuilder-dist ${RELEASE} ${ARCH} build \
    --buildresult /packages/${DISTRO}/${RELEASE}/${ARCH} *${RELEASE}*.dsc
done;
