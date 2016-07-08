from elasticsearch import RequestsHttpConnection
from elasticsearch.client import Elasticsearch
from elasticsearch.exceptions import ElasticsearchException

def new_elasticsearch():

    Elasticsearch(host='171.30.151.164',
                          port=9200,
                          use_ssl=True,
                          connection_class=RequestsHttpConnection,
                          timeout=10,
                          # ca_certs='/opt/secrets/ea.ca',
                          # client_cert='/opt/secrets/ea.cert',
                          # client_key='/opt/secrets/ea.key',
                          # )
                          
 new_elasticsearch()

 # https://192:9200/logstash-*/_search?_source_include=%40timestamp%2C%2A&ignore_unavailable=true&size=10000
 
 # https://172.30.151.164:9200/api-factory-asia-qa*/_search?_source_include=%40timestamp%2C%2A&ignore_unavailable=true&size=10000