#!/bin/bash

pip install -q -e .
while ! echo exit | curl -s localhost:9200; do sleep 10; done
curl -s -H'Content-Type: application/json' -XPOST localhost:9200/logstash-12.12.2012/log/_bulk --data-binary @<(sed 's/^/{"index": {}}\n&/' tests/es_data/docs.json) | jq .
curl -s -H'Content-Type: application/json' -XPOST localhost:9200/unicode-logstash-12.12.2012/log/_bulk --data-binary @<(sed 's/^/{"index": {}}\n&/' tests/es_data/docs_with_unicode.json) | jq .
tail -f /var/log/elasticsearch.log
