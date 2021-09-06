import json
import logging

from flask import request

from api.server import app
from elastic.es_wrapper import get_book_by_id, get_user_books
from logic.wrapper_recommender import WrapperRecommender


@app.route('/recommend/')
def recommend():
    """
    Gives recommended books for given user_id
    :return: list of books from elasticsearch database
    """
    user_id = request.args.get('user_id')
    if user_id:
        to_ret = []
        list_of_recommendations = WrapperRecommender().recommend(user_id)
        if len(list_of_recommendations):
            for rec in list_of_recommendations:
                to_ret.append(
                    get_book_by_id(rec)
                )
        logging.info(f"User: {user_id}, {len(to_ret)} books sent as recommendation")
        return json.dumps(to_ret), 200, {'ContentType': 'application/json'}
    else:
        return "", 200, {'ContentType': 'application/json'}


@app.route('/record/', methods=['POST', 'GET'])
def add_record():
    """
    Adds new favourite book to user specified in user_id
    """
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if book_id and not user_id:
        user_id = WrapperRecommender().register_new_user()
    if user_id and book_id:
        WrapperRecommender().record(user_id, book_id)
        return json.dumps({'success': True, 'user_id': str(user_id)}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@app.route('/record/', methods=['DELETE'])
def drop_record():
    """
    TODO Refactor recommender to support delete
    Deletes user book record from elasticsearch database
    """
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if book_id and user_id:
        WrapperRecommender().drop_record(user_id, book_id)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@app.route('/get_user_favourite/')
def get_user_history():
    """
    Gets users favourite books from elasticsearch
    """
    user_id = request.args.get('user_id')
    if user_id:
        to_ret = []
        user_books = get_user_books(user_id)

        list_of_ids = [book_id['_source']['book_id'] for book_id in user_books]
        if len(list_of_ids) > 0:
            for rec in list_of_ids:
                to_ret.append(
                    get_book_by_id(rec)
                )
        logging.info(f"User: {user_id}, {len(to_ret)} books sent as favourite")
        return json.dumps(to_ret), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


@app.route('/get_user_number')
def get_user_number():
    """
    **DEPRECATED**
        User must add books immediately after to register this user_id
        This can cause concurrent modification error

    Gives user_id to a new user
    """
    user_id = WrapperRecommender().register_new_user()
    return str(user_id)
