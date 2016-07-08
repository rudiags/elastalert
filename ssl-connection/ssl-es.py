# encoding: utf-8
from elasticsearch import RequestsHttpConnection
from elasticsearch.client import Elasticsearch
from elasticsearch.exceptions import ElasticsearchException

ES_IP = '172.30.151.164'

def new_elasticsearch():

    try:
        es = Elasticsearch(host=ES_IP,
                              port=9200,
                              use_ssl=True,
                              connection_class=RequestsHttpConnection,
                              timeout=10,
                              ca_certs='/opt/secrets/ea.ca',
                              verify_certs=True,
                              client_cert='/opt/secrets/ea.crt',
                              client_key='/opt/secrets/ea.key',
                              )

        logs = es.search(index='api-factory-asia-qa*', q='_source_include=%40timestamp%2C%2A&ignore_unavailable=true&size=10000')
        print logs
    except ElasticsearchException as e:
        print "\n\n\n[ElasticsearchError]", e

new_elasticsearch()