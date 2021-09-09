import os

from elastic.es_wrapper import get_user_with_max_user_id, load_index_from_elasticsearch
from elastic.instance import es
from logic.recommender import Recommender
from elastic.es_wrapper import get_list_of_books_indexes_of_user
import logging

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WrapperRecommender(metaclass=Singleton):
    """
    Singleton object

    Is an abstraction of recommender class
    """

    def __init__(self,
                 n_people=10000,
                 n_books=10000,
                 load_data_from_elastic=True):
        """
        :param n_people: Maximum number of users to handle
        :param n_books: Maximum number of books to handle
        :param load_data_from_elastic:
                    True - loads data from elasticsearch to model
        """
        self.recommender = Recommender(n_books, n_people)
        if load_data_from_elastic:
            self.load_index_from_elastic_to_model(os.environ['USERS_BOOKS_INDEX'])

    def record(self, user_id, book_id, add_to_elastic=True):
        if add_to_elastic and book_id in get_list_of_books_indexes_of_user(user_id):
            # book_id is already in database
            logging.info("Book is already in database")
            return
        self.recommender.record(book_id, user_id)
        if add_to_elastic:
            es.index(os.environ['USERS_BOOKS_INDEX'], body={'user_id': user_id, 'book_id': book_id})

    def recommend(self, person_id):
        last_read = get_list_of_books_indexes_of_user(person_id)
        recs = []
        if len(last_read) > 0:
            recs = self.recommender.recommend(last_read[-1], person_id)
        return recs

    def drop_record(self, user_id, book_id):
        """
        TODO Functionality needs to be added to recommender
        :param user_id:
        :param book_id:
        :return:
        """
        res = es.search(index=os.environ['USERS_BOOKS_INDEX'], body={
            "query": {
                "bool": {

                    "must": [
                        {"term": {"user_id": user_id}},

                    ]
                }
            }
        })['hits']['hits']
        for result in res:
            if result['_source']['book_id'] == book_id:
                es.delete(index=os.environ['USERS_BOOKS_INDEX'], id=result['_id'])
                break

    def get_person_history(self, person_id):
        return self.recommender.person_history(person_id)

    @staticmethod
    def register_new_user():
        # Idea is simple - find last number, and assign next to user
        res = get_user_with_max_user_id()
        last_id = int(res['hits']['hits'][0]['_source']['user_id'])
        return last_id + 1

    def load_index_from_elastic_to_model(self, index_name):
        resp = load_index_from_elasticsearch(index_name)
        for doc in resp:
            self.record(doc['_source']['user_id'], doc['_source']['book_id'], add_to_elastic=False)
