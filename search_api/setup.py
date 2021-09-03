import logging
import os
import sys
import time

from config import parse_args

time.time()

if __name__ == '__main__':
    logging.info("Initializing worker setup.py")
    parse_args(sys.argv)
    if os.environ['SCRAP_WEBPAGE'] == 'True':
        # TODO Add Scrapping
        # Assumes that scarping returns csv in folder raw_data
        pass
    if os.environ['BUILD_ELASTIC'] == 'True':
        from elastic.init_elasticsearch import create_index_and_fill_with_data

        """
        Initializes Elasticsearch db with data
        Needs raw_data/books.csv and raw_data/users_and_books.csv files 
        """
        from process_data.process_data import convert_csv_to_json, convert_users_csv_to_json
        logging.info("Starting convert_csv_to_json on books")
        books_json_path = convert_csv_to_json(os.environ['PATH_TO_BOOKS'])

        logging.info("Starting create_index_and_fill_with_data on books")
        create_index_and_fill_with_data('books_index', os.environ['PATH_TO_BOOKS'].replace(".csv", ".json"),
                                        'assets/books_index_def.json')
                                        
        logging.info("Starting convert_users_csv_to_json on users")
        users_json_path = convert_users_csv_to_json(os.environ['PATH_TO_USERS'])

        logging.info("Starting create_index_and_fill_with_data on users")
        create_index_and_fill_with_data('users_and_books',
                                        os.environ['PATH_TO_USERS'].replace(".csv",
                                                                            ".json"),
                                        'assets/users_and_books.json')

    if os.environ['RUN_FLASK_WSGI'] == 'True':
        from api.server import run_server

        run_server()
    logging.info("Successfully finished worker job")
