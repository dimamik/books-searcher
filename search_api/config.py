import logging
import os
import re

from env import credentials


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
    """
    Replace credentials with your username and password
    Used in https://www.litmir.me/
    This is used in scraping
    """
    os.environ['SCRAP_WEBPAGE'] = 'False'
    os.environ['BUILD_ELASTIC'] = 'False'
    os.environ['BOOKS_INDEX'] = 'books_index'
    os.environ['USERNAME'] = credentials.username
    os.environ['PASSWORD'] = credentials.password
    os.environ['PATH_TO_BOOKS'] = 'raw_data/books.csv'
    os.environ['PATH_TO_USERS'] = 'raw_data/users_and_books.csv'
    os.environ['ELASTIC_HOST'] = 'elasticsearch'
    os.environ['ELASTIC_PORT'] = '9200'
    os.environ['SERVER_HOST'] = 'localhost'
    os.environ['SERVER_PORT'] = '5000'
    os.environ['RUN_SERVER'] = 'True'


if __name__ == "__main__":
    init_config()
