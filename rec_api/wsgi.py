from config import init_config, init_logging
from api.server import *
# app instance from api.server is used to feed uwsgi config
# config is imported first to initialize variables

# init the size of recommender at the begining

# WOULD FAIL IF THERE IS NO DATABASE AND IT IS OKAY!
from recommender_logic.wrapper_recommender import WrapperRecommender

WrapperRecommender(
    int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))
# TODO THIS FILE IS REALLY WEAK, FIX IT

if __name__ == '__main__':
    init_config()
    init_logging()
    # This section is never run when using uwsgi scripts
    run_server()
