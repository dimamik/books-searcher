import json

from flask import request

from api.server import app
from setup import recommender


@app.route('/recommend/<user_id>')
def recommend(user_id):
    return str(recommender.recommend(user_id))


@app.route('/record/', methods=['POST'])
def add_record():
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if user_id and book_id:
        recommender.record(user_id, book_id)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/record/', methods=['DELETE'])
def drop_record():
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if book_id and user_id:
        print(recommender.drop_record(user_id, book_id))

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get_user_history/<user_id>')
def get_user_history(user_id):
    return str(recommender.get_person_history(user_id))


@app.route('/register_user')
def register_user():
    user_id = recommender.register_new_user()
    return str(user_id)
