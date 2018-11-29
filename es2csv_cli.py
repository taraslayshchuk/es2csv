#!/usr/bin/env python
"""
title:           A CLI tool for exporting data from Elasticsearch into a CSV file.
description:     Command line utility, written in Python, for querying Elasticsearch in Lucene query syntax or Query DSL syntax and exporting result as documents into a CSV file.
usage:           es2csv -q '*' -i _all -e -o ~/file.csv -k -m 100
                 es2csv -q '{"query": {"match_all": {}}}' -r -i _all -o ~/file.csv
                 es2csv -q @'~/long_query_file.json' -r -i _all -o ~/file.csv
                 es2csv -q '*' -i logstash-2015-01-* -f host status message -o ~/file.csv
                 es2csv -q 'host: localhost' -i logstash-2015-01-01 logstash-2015-01-02 -f host status message -o ~/file.csv
                 es2csv -q 'host: localhost AND status: GET' -u http://kibana.com:80/es/ -o ~/file.csv
                 es2csv -q '*' -t dev prod -u http://login:password@kibana.com:6666/es/ -o ~/file.csv
                 es2csv -q '{"query": {"match_all": {}}, "filter":{"term": {"tags": "dev"}}}' -r -u http://login:password@kibana.com:6666/es/ -o ~/file.csv
"""
import sys
import argparse
import es2csv

__version__ = '5.5.2'


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('-q', '--query', dest='query', type=str, required=True, help='Query string in Lucene syntax.')
    p.add_argument('-u', '--url', dest='url', default='http://localhost:9200', type=str, help='Elasticsearch host URL. Default is %(default)s.')
    p.add_argument('-a', '--auth', dest='auth', type=str, required=False, help='Elasticsearch basic authentication in the form of username:password.')
    p.add_argument('-i', '--index-prefixes', dest='index_prefixes', default=['logstash-*'], type=str, nargs='+', metavar='INDEX', help='Index name prefix(es). Default is %(default)s.')
    p.add_argument('-D', '--doc-types', dest='doc_types', type=str, nargs='+', metavar='DOC_TYPE', help='Document type(s).')
    p.add_argument('-t', '--tags', dest='tags', type=str, nargs='+', help='Query tags.')
    p.add_argument('-o', '--output-file', dest='output_file', type=str, required=True, metavar='FILE', help='CSV file location.')
    p.add_argument('-f', '--fields', dest='fields', default=['_all'], type=str, nargs='+', help='List of selected fields in output. Default is %(default)s.')
    p.add_argument('-S', '--sort', dest='sort', default=[], type=str, nargs='+', metavar='FIELDS', help='List of <field>:<direction> pairs to sort on. Default is %(default)s.')
    p.add_argument('-d', '--delimiter', dest='delimiter', default=',', type=str, help='Delimiter to use in CSV file. Default is "%(default)s".')
    p.add_argument('-m', '--max', dest='max_results', default=0, type=int, metavar='INTEGER', help='Maximum number of results to return. Default is %(default)s.')
    p.add_argument('-s', '--scroll-size', dest='scroll_size', default=100, type=int, metavar='INTEGER', help='Scroll size for each batch of results. Default is %(default)s.')
    p.add_argument('-k', '--kibana-nested', dest='kibana_nested', action='store_true', help='Format nested fields in Kibana style.')
    p.add_argument('-kd', '--kibana-delimiter', dest='kibana_delimiter', type=str, required=False, default=',', help='Delimiter for Kibana Style')
    p.add_argument('-r', '--raw-query', dest='raw_query', action='store_true', help='Switch query format in the Query DSL.')
    p.add_argument('-e', '--meta-fields', dest='meta_fields', action='store_true', help='Add meta-fields in output.')
    p.add_argument('--verify-certs', dest='verify_certs', action='store_true', help='Verify SSL certificates. Default is %(default)s.')
    p.add_argument('--ca-certs', dest='ca_certs', default=None, type=str, help='Location of CA bundle.')
    p.add_argument('--client-cert', dest='client_cert', default=None, type=str, help='Location of Client Auth cert.')
    p.add_argument('--client-key', dest='client_key', default=None, type=str, help='Location of Client Cert Key.')
    p.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__, help='Show version and exit.')
    p.add_argument('--debug', dest='debug_mode', action='store_true', help='Debug mode on.')

    if len(sys.argv) == 1:
        p.print_help()
        exit()

    opts = p.parse_args()
    es = es2csv.Es2csv(opts)
    es.create_connection()
    es.check_indexes()
    es.search_query()
    es.write_to_csv()
    es.clean_scroll_ids()


if __name__ == '__main__':
    main()
