import os

from elasticsearch import Elasticsearch

# To use safely environment variables
import config

es = Elasticsearch([{'host': os.environ['ELASTIC_HOST'],
                     'port': os.environ['ELASTIC_PORT']}])

if __name__ == '__main__':
    config.init_logging()
