import json

from flask import request

from api.server import app
from elastic.books_getter import get_book_by_id
from recommender_logic.wrapper_recommender import WrapperRecommender


@app.route('/recommend/')
def recommend():
    user_id = request.args.get('user_id')
    if user_id:
        to_ret = []
        list_of_recommendations = WrapperRecommender().recommend(user_id)
        if len(list_of_recommendations):
            for rec in list_of_recommendations:
                to_ret.append(
                    get_book_by_id(rec)
                )
        return json.dumps(to_ret), 200, {'ContentType': 'application/json'}
    else:
        return "", 200, {'ContentType': 'application/json'}


@app.route('/record/', methods=['POST', 'GET'])
def add_record():
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if user_id and book_id:
        WrapperRecommender().record(user_id, book_id)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/record/', methods=['DELETE'])
def drop_record():
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if book_id and user_id:
        print(WrapperRecommender().drop_record(user_id, book_id))

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get_user_favourite/')
def get_user_history():
    user_id = request.args.get('user_id')
    if user_id:
        to_ret = []
        list_of_recommendations = WrapperRecommender().get_person_history(user_id)
        if len(list_of_recommendations):
            for rec in list_of_recommendations:
                to_ret.append(
                    get_book_by_id(rec)
                )
        return json.dumps(to_ret), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@app.route('/get_user_number')
def get_user_number():
    user_id = WrapperRecommender().register_new_user()
    return str(user_id)
