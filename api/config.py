import os
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def init_config():
    os.environ['INDEX_NAME'] = 'db_books'
    os.environ['BUILD_ELASTIC'] = "True"



if __name__ == "__main__":
    init_config()
