import os
import sys

# Config is initialized with import
import config

if __name__ == '__main__':
    config.parse_args(sys.argv)
    # Init singleton object
    from recommender_logic.wrapper_recommender import WrapperRecommender
    WrapperRecommender(
        int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))

    from api.server import run_server

    run_server()
