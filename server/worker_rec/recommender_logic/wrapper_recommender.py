import urllib.request

from recommender_logic.recommender import Recommender


def load_data_from_csv():
    # TODO Change request to be paginated and so on
    # First column is persons, second - books
    urllib.request.urlretrieve('http://127.0.0.1:5000/get_all_index/users_and_books', 'downloaded_users.csv')
    pass


class WrapperRecommender:
    def __init__(self, n_people, n_books):
        self.recommender = Recommender(n_books, n_people)
        # Make it lazy-loaded
        load_data_from_csv()
        self.train_recommender()

    def record(self, user_id, book_hash):
        self.recommender.record(book_hash, user_id)

    def recommend(self, person_id):
        last_read = self.recommender.person_history(person_id)
        recs = []
        if len(last_read) > 0:
            recs = self.recommender.recommend(last_read[-1], person_id)
        return recs

    def record(self, person_id, document_id):
        self.recommender.record(document_id, person_id)

    def train_recommender(self):
        import csv
        with open('downloaded_users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                self.record(row[1], row[2])
                pass
