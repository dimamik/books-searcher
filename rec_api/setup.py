from recommender_logic.wrapper_recommender import WrapperRecommender
from config import init_config, parse_args, init_logging
import os
import sys


if __name__ == '__main__':
    init_logging()
    init_config()
    parse_args(sys.argv)
# Init singleton object
    WrapperRecommender(
        int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))
