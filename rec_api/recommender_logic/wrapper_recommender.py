import os

from elasticsearch import helpers

from elastic.instance import es
from recommender_logic.recommender import Recommender


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WrapperRecommender(metaclass=Singleton):
    def __init__(self,
                 n_people=os.environ['USERS_MAX_N'],
                 n_books=os.environ['BOOKS_MAX_N']):
        self.recommender = Recommender(n_books, n_people)
        # Make it lazy-loaded
        self.load_index_from_elasticsearch_database(os.environ['USERS_BOOKS_INDEX'])

    def record(self, user_id, book_id, add_to_elastic=True):
        # Check if data is not already in database
        if book_id in self.get_person_history(user_id):
            return
        self.recommender.record(book_id, user_id)
        if add_to_elastic:
            es.index(os.environ['USERS_BOOKS_INDEX'], body={'user_id': user_id, 'book_id': book_id})

    def recommend(self, person_id):
        last_read = self.recommender.person_history(person_id)
        recs = []
        if len(last_read) > 0:
            recs = self.recommender.recommend(last_read[-1], person_id)
        return recs

    def drop_record(self, user_id, book_id):
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
            else:
                raise Exception("No such _id")

    def get_person_history(self, person_id):
        return self.recommender.person_history(person_id)

    def register_new_user(self):
        #     Idea is simple - find last number, and assign next to user
        # TODO FIX logic of "registration"
        res = es.search(
            index=os.environ['USERS_BOOKS_INDEX'],
            size=1,
            body={
                "sort": {
                    "user_id": "desc"
                }
            },
        )
        last_id = int(res['hits']['hits'][0]['_source']['user_id'])
        last_id += 1
        return last_id

    def load_index_from_elasticsearch_database(self, index_name):
        resp = helpers.scan(
            es,
            index=index_name,
            scroll='1m',
            size=100,
        )

        # enumerate the documents
        for num, doc in enumerate(resp):
            self.record(doc['_source']['user_id'], doc['_source']['book_id'], add_to_elastic=False)
