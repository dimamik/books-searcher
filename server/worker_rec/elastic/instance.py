import os

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': os.environ['ELASTIC_HOST'],
                     'port': int(os.environ['ELASTIC_PORT'])}])
