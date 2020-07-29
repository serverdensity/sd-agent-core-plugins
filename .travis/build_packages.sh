#!/bin/bash
echo "${RELEASE}"
DEFAULT_DOCKERFILE_DIR=".travis/dockerfiles/"
if [[ "$TRAVIS_TAG" ]]; then
    PACKAGES_DIR="/${TRAVIS_REPO_SLUG}/${TRAVIS_TAG}/"
else
    PACKAGES_DIR="/${TRAVIS_REPO_SLUG}/${TRAVIS_BUILD_ID}/"
fi

deb=(bionic buster focal xenial trusty jessie stretch)
CONTAINER="$RELEASE"
echo "$CONTAINER"
set -ev

rvm install 2.1.5
bundle install
bundle exec rake copy_checks

if [ -f "${TRAVIS_BUILD_DIR}/config.py" ]; then
   AGENT_VERSION=$(awk -F'"' '/^AGENT_VERSION/ {print $2}' ${TRAVIS_BUILD_DIR}/config.py)
elif [[ -z "${AGENT_VERSION}" ]]; then
   echo "Cannot establish AGENT_VERSION. Exiting"
   exit 1
fi

echo "Agent Version: ${AGENT_VERSION}"

#cd "${1:-$DEFAULT_DOCKERFILE_DIR}"

#Create required folders if they do not already exist
if [ ! -d "$PACKAGES_DIR" ]; then
    sudo mkdir -p "$PACKAGES_DIR"
fi
if [ ! -d "$CACHE_DIR" ]; then
    sudo mkdir "$CACHE_DIR"
fi

# Load the containers from cache

CACHE_FILE_VAR="CACHE_FILE_${CONTAINER}"
DOCKER_CACHE=${!CACHE_FILE_VAR}
echo "$DOCKER_CACHE"
find "$CACHE_DIR"
gunzip -c "$DOCKER_CACHE" | docker load;


# Run the containers, if container name is bionic run with --privileged
echo "$CONTAINER"
echo "$RELEASE"
if [[ ${deb[*]} =~ "$RELEASE" ]]; then
    sudo docker run --volume="${TRAVIS_BUILD_DIR}":/sd-agent:rw --volume="${PACKAGES_DIR}":/packages:rw -e RELEASE="${RELEASE}" --privileged serverdensity:"${CONTAINER}"
else
    sudo docker run --volume="${TRAVIS_BUILD_DIR}":/sd-agent-core-plugins:rw --volume="${PACKAGES_DIR}":/packages:rw -e sd_agent_version="${AGENT_VERSION}" serverdensity:"${CONTAINER}"
fi

sudo find "$PACKAGES_DIR"
