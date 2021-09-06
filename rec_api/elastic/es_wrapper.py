import os

from elasticsearch import helpers

from elastic.instance import es


def result_selector(result):
    """
    TODO
    Selects needed fields in result output
    of elasticsearch
    :param result:
    :return:
    """
    return result


def get_book_by_id(book_id):
    res = es.get(
        index=os.environ['BOOKS_INDEX'],
        id=book_id
    )
    return res


def get_user_books(user_id):
    res = es.search(
        index=os.environ['USERS_BOOKS_INDEX'],
        body={
            "query": {
                "query_string": {
                    "query": f"{user_id}",
                    "fields": ['user_id']
                }
            },
        }
    )
    return res['hits']['hits']


def get_user_with_max_user_id():
    return es.search(
        index=os.environ['USERS_BOOKS_INDEX'],
        size=1,
        body={
            "sort": {
                "user_id": "desc"
            }
        },
    )


def load_index_from_elasticsearch(index_name,
                                  chunk_size=100):
    return helpers.scan(
        es,
        index=index_name,
        scroll='1m',
        size=chunk_size,
    )
