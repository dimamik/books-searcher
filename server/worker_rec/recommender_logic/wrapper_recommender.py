from recommender_logic.recommender import Recommender


class WrapperRecommender():
    def __init__(self, n_people, n_books):
        self.recommender = Recommender(n_books, n_people)

    def record(self, user_id, book_hash):
        self.recommender.record(book_hash, user_id)

    def recommend(self, person_id):
        last_read = self.recommender.person_history(person_id)
        recs = []
        if (len(last_read) > 0):
            recs = self.recommend.recommend(last_read[-1], person_id)
        return recs

    def load_csv_data(self, path, person_id_index=0, book_name_index=1):
        

    @lazyprop
    def recommender(self):
        return self.recommender
