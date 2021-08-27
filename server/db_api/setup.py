import logging
import os
import time

from api.server import run_server
from config import init_config
from elastic.init_elasticsearch import create_index_and_fill_with_data

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
from process_data.process_data import convert_users_csv_to_json, convert_csv_to_json

init_config()
time.time()

if __name__ == '__main__':
    # run scarp if there is no data in folder data
    if os.environ['SCARP_WEBPAGE'] == 'True':
        # TODO Add Scarping
        # Assumes that scarping returns csv in folder raw_data
        pass
    # Initialize and fill elasticsearch with data if needed
    if os.environ['BUILD_ELASTIC'] == 'True':
        # Convert csv to json and filter data
        books_json_path = convert_csv_to_json(os.environ['PATH_TO_BOOKS'])
        create_index_and_fill_with_data('books_index', os.environ['PATH_TO_BOOKS'].replace(".csv", ".json"),
                                        'assets/books_index_def.json')

        # users_json_path = convert_users_csv_to_json(os.environ['PATH_TO_USERS'])
    create_index_and_fill_with_data('users_and_books',
                                    os.environ['PATH_TO_USERS'].replace(".csv",
                                                                        ".json"),
                                    'assets/users_and_books.json')

    run_server()
