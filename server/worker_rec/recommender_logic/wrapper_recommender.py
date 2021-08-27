from elasticsearch import helpers

from elastic.instance import es
from recommender_logic.recommender import Recommender

INDEX_NAME = 'users_and_books'


class WrapperRecommender:
    def __init__(self, n_people, n_books):
        self.recommender = Recommender(n_books, n_people)
        # Make it lazy-loaded
        self.load_index_from_elasticsearch_database(INDEX_NAME)

    def record(self, user_id, book_id, add_to_elastic=True):
        self.recommender.record(book_id, user_id)
        if add_to_elastic:
            es.index(INDEX_NAME, body={'user_id': user_id, 'book_id': book_id})

    def recommend(self, person_id):
        last_read = self.recommender.person_history(person_id)
        recs = []
        if len(last_read) > 0:
            recs = self.recommender.recommend(last_read[-1], person_id)
        return recs

    def drop_record(self, user_id, book_id):
        res = es.search(index=INDEX_NAME, body={
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
                es.delete(index=INDEX_NAME, id=result['_id'])
                break
            else:
                raise Exception("No such _id")

    def get_person_history(self, person_id):
        return self.recommender.person_history(person_id)

    def register_new_user(self):
        #     Idea is simple - find last number, and assign next to user
        # TODO FIX logic of "registration"
        res = es.search(
            index=INDEX_NAME,
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
        # TODO This is temporary solution, move it to db_api!

        # call the helpers library's scan() method to scroll
        resp = helpers.scan(
            es,
            index=index_name,
            scroll='1m',
            size=100,
        )

        # enumerate the documents
        for num, doc in enumerate(resp):
            self.record(doc['_source']['user_id'], doc['_source']['book_id'], add_to_elastic=False)
