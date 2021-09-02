import logging
import os

import re


def init_logging():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def parse_args(args):
    args = args[1:]
    for arg in args:
        try:
            arg = re.sub("['\" ]", "", arg)
            key, value = arg.split("=")
            os.environ[key] = value
        except ValueError:
            logging.error("Bad format of parameters\n"
                          "Proper way is: "
                          "python setup.py SERVER_HOST=localhost")


def init_config():
    os.environ['BOOKS_INDEX'] = 'books_index'
    os.environ['USERS_BOOKS_INDEX'] = 'users_and_books'
    os.environ['USERS_MAX_N'] = '10000'
    os.environ['BOOKS_MAX_N'] = '10000'
    os.environ['ELASTIC_HOST'] = 'elasticsearch'
    os.environ['ELASTIC_PORT'] = '9200'
    os.environ['SERVER_HOST'] = 'rec_api'
    os.environ['SERVER_PORT'] = '5001'


init_config()
init_logging()

if __name__ == "__main__":
    init_config()
