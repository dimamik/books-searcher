import os
import sys

import config
# config is initialized when imported
from recommender_logic.wrapper_recommender import WrapperRecommender

if __name__ == '__main__':
    config.parse_args(sys.argv)
    # Init singleton object
    WrapperRecommender(
        int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))

    from api.server import run_server

    run_server()
