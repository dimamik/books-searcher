import sys

import config
from api.server import *
# WOULD BREAK IF THERE IS NO DATABASE AND IT IS OKAY!
from recommender_logic.wrapper_recommender import WrapperRecommender

# app instance from api.server is used to feed uwsgi config
# config is imported first to initialize variables
# init the size of recommender at the beginning

WrapperRecommender(
    int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))

if __name__ == '__main__':
    # This section is never run when using uwsgi scripts
    config.parse_args(sys.argv)
    run_server()
