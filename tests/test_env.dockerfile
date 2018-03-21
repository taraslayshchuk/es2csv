ARG ES_VERSION
FROM docker.elastic.co/elasticsearch/elasticsearch:${ES_VERSION}

USER root
RUN echo 'timeout=1'>> /etc/yum.conf && \
    yum install epel-release -y -q && \
    yum install procps python jq -y -q && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    curl -L "https://bootstrap.pypa.io/get-pip.py" | python - && \
    curl -L "https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz" | tar xz -C "/tmp" && \
    bash /tmp/bats-0.4.0/install.sh /usr/local && \
    rm -rf /tmp/bats-0.4.0 && \
    echo 'xpack.security.enabled: false' >> /usr/share/elasticsearch/config/elasticsearch.yml

WORKDIR /data
