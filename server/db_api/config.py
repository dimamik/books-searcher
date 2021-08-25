import os

from env import credentials


def init_config():
    os.environ['SCARP_WEBPAGE'] = 'False'
    os.environ['BUILD_ELASTIC'] = 'False'
    os.environ['BOOKS_INDEX'] = 'books_index'
    # Replace credentials with your username and password
    os.environ['USERNAME'] = credentials.username
    os.environ['PASSWORD'] = credentials.password
    os.environ['PATH_TO_BOOKS'] = 'raw_data/books.csv'
    os.environ['PATH_TO_USERS'] = 'raw_data/users_and_books.csv'


if __name__ == "__main__":
    init_config()
