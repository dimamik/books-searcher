import sys

import config
from api.server import *
from logic.wrapper_recommender import WrapperRecommender

# app instance from api.server is used to feed uwsgi config
# config is imported first to initialize variables
# init the size of recommender at the beginning
# elasticsearch needs to be running to load model with data

# TODO Drop Privileges of uwsgi when running!

WrapperRecommender(
    int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))

if __name__ == '__main__':
    # This is never run when using uwsgi scripts
    config.parse_args(sys.argv)
    run_server()
