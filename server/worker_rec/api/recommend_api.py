from api.server import app
from setup import recommender


@app.route('/recommend/<user_id>')
def recommend(user_id):
    return str(recommender.recommend(user_id))


@app.route('/record')
def upload_index():
    # TODO Extract values from parameters

    pass


@app.route('/get_user_history/<user_id>')
def person_history(user_id):
    return str(recommender.recommender.person_history(user_id))
