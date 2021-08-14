import sys
from elasticsearch import Elasticsearch, helpers
import requests
import json
import os
import re
from elasticsearch import Elasticsearch
import pprint
import functools

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def filter_query(query):
    query = " ".join(query.split())
    query = ''.join(filter(lambda char: str.isdigit(char)
                           or str.isalpha(char) or char == " ", query))
    return query


def clean_response(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_clean_response(*args, **kwargs):

        result = func(*args, **kwargs)
        # TODO There result needs to be cleaned
        return result
    return wrapper_clean_response


@clean_response
def search_as_you_type(query):
    return es.search(index='books', body={
        "query": {
            "multi_match": {
                "query": filter_query(query),
                "type": "bool_prefix",
                "fields": [
                        "book_name^4", "book_author^3"
                ]
            }
        },
        "size": 10,
        "from": 0
    }
    )


@clean_response
def search(query):
    return es.search(index='books', body={
        "query": {
            "query_string": {
                "query": f"*{filter_query(query)}*",
                "fields": ["book_name^3", "book_author^2", "book_description"]
            }
        },
        "size": 10,
        "from": 0
    }
    )


if __name__ == "__main__":
    search("Hello")
