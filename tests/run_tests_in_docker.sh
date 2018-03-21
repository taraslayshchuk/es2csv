#!/bin/bash
set -e

while getopts "be:" opt; do
    case "$opt" in
        b) BUILD_IMAGE=1 ;;
        e) ES_VERSION=$OPTARG ;;
    esac
done
shift $((OPTIND-1))

if [ ! "$ES_VERSION" ]; then
    echo 'Elasticsearch version(-e) required.'
    exit 1
fi

if [[ $BUILD_IMAGE == 1 ]]; then
    echo "+++ Docker building build image..."
    cat ./tests/test_env.dockerfile | docker build --tag es2csv_test_env:"${ES_VERSION}" --build-arg ES_VERSION="${ES_VERSION}" -
    echo "+++ Done."
fi

echo "+++ Docker running tests in docker..."
docker run -it --rm \
       -v `pwd`:/data \
       es2csv_test_env:"${ES_VERSION}" \
       /bin/bash -c 'su elasticsearch "/usr/share/elasticsearch/bin/elasticsearch" > /var/log/elasticsearch.log 2>&1 & \
                    ./tests/test.sh'
echo "+++ Done."
