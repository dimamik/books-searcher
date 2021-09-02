from config import init_config, parse_args, init_logging
# config is initialized when imported
from recommender_logic.wrapper_recommender import WrapperRecommender
import os
import sys


if __name__ == '__main__':
    parse_args(sys.argv)
# Init singleton object
    WrapperRecommender(
        int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))
