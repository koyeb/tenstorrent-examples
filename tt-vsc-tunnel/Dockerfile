ARG BASE_IMAGE=ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-release-amd64:latest-rc

FROM ${BASE_IMAGE}

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-utils \
    ca-certificates \
    openssh-client \
    iptables \
    gnupg \
    software-properties-common \
    wget \
    libc6 \
    libstdc++6 \
    curl \
    bash \
    git \
    vim \
    iptables && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/debconf/* /var/log/* /tmp/* /var/tmp/*

# Docker

RUN mkdir -pm755 /etc/apt/keyrings && curl -o /etc/apt/keyrings/docker.asc -fsSL "https://download.docker.com/linux/ubuntu/gpg" && chmod a+r /etc/apt/keyrings/docker.asc && \
    mkdir -pm755 /etc/apt/sources.list.d && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(grep UBUNTU_CODENAME= /etc/os-release | cut -d= -f2 | tr -d '\"') stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && apt-get install --no-install-recommends -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    pigz \
    xz-utils && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/debconf/* /var/log/* /tmp/* /var/tmp/*

COPY --from=docker:dind /usr/local/bin/docker-init /usr/local/bin/docker-init

# https://github.com/docker-library/docker
ADD https://raw.githubusercontent.com/docker-library/docker/master/modprobe.sh /usr/local/bin/modprobe
ADD https://raw.githubusercontent.com/docker-library/docker/master/dockerd-entrypoint.sh /usr/local/bin/
ADD https://raw.githubusercontent.com/docker-library/docker/master/docker-entrypoint.sh /usr/local/bin/
ADD https://raw.githubusercontent.com/moby/moby/master/hack/dind /usr/local/bin/dind

ADD https://raw.githubusercontent.com/koyeb/koyeb-docker-compose/refs/heads/master/koyeb-entrypoint.sh /usr/local/bin/koyeb-entrypoint.sh

RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh /usr/local/bin/docker-entrypoint.sh /usr/local/bin/dind /usr/local/bin/koyeb-entrypoint.sh

VOLUME /var/lib/docker

# VSCode

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' | tar -xz -C /usr/local/bin

WORKDIR /workdir

ENV VSC_NODE_NAME=${VSC_NODE_NAME:-tt-on-koyeb}

ENTRYPOINT ["/usr/local/bin/koyeb-entrypoint.sh"]

CMD code tunnel --name "$VSC_NODE_NAME" --accept-server-license-terms