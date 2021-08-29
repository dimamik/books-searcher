import functools
import os

from elasticsearch import Elasticsearch

from process_data.string_filter import filter_book_name, filter_query

es = Elasticsearch([{'host': os.environ['ELASTIC_HOST'],
                     'port': os.environ['ELASTIC_PORT']}])


def clean_response(func):
    @functools.wraps(func)
    def wrapper_clean_response(*args, **kwargs):
        result = func(*args, **kwargs)
        # TODO Clean Results
        return result

    return wrapper_clean_response


@clean_response
def search_as_you_type(query):
    """
    Returns search results on filtered query containing all
    fields except description, search_as_you_type fields are used
    """
    return es.search(index=os.environ['BOOKS_INDEX'], body={
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
    }, filter_path=[
        'hits.hits._source.book_author',
        'hits.hits._source.book_genre',
        'hits.hits._source.book_name',
        'hits.hits._source.book_points',
        'hits.hits._id'
    ])


@clean_response
def search(query):
    """
    Usual search on filtered query
    """
    return es.search(index=os.environ['BOOKS_INDEX'], body={
        "query": {
            "query_string": {
                "query": f"*{filter_query(query)}*",
                "fields": ["book_name^3", "book_author^2", "book_description"]
            }
        },
        "size": 10,
        "from": 0
    }, filter_path=['hits.hits._source', 'hits.hits._id'])


def find_book_id_by_book_name(book_name):
    book_name = filter_book_name(book_name)
    res = es.search(index=os.environ['BOOKS_INDEX'], body={
        "query": {
            "query_string": {
                "query": f"*{filter_query(book_name)}*",
                "fields": ["book_name"]
            }
        },
        "size": 1,
        "from": 0
    })
    if len(res['hits']['hits']) > 0:
        # There are results
        if book_name == res['hits']['hits'][0]['_source']['book_name']:
            return res['hits']['hits'][0]['_id']
    return None
