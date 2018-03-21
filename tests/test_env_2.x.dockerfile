# Backup for elasticsearch-docker:2.x
ARG ES_VERSION
FROM elasticsearch:${ES_VERSION}

RUN apt-get update -qq && \
    apt-get install -qqy procps python jq && \
    apt-get clean -qq && \
    rm -rf /var/lib/apt/lists/* && \
    curl -L "https://bootstrap.pypa.io/get-pip.py" | python - && \
    curl -L "https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz" | tar xz -C "/tmp" && \
    bash /tmp/bats-0.4.0/install.sh /usr/local && \
    rm -rf /tmp/bats-0.4.0

WORKDIR /data
