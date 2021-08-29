import os
import sys

from config import init_config, parse_args, init_logging


def main():
    init_logging()
    init_config()
    parse_args(sys.argv)
    from recommender_logic.wrapper_recommender import WrapperRecommender
    # Init singleton object
    WrapperRecommender(
        int(os.environ['USERS_MAX_N']), int(os.environ['BOOKS_MAX_N']))
    from api.server import run_server
    run_server()


if __name__ == '__main__':
    main()
