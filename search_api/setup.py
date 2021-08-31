import os
import sys
import time

from config import init_config, init_logging, parse_args

time.time()

if __name__ == '__main__':
    init_logging()
    init_config()
    parse_args(sys.argv)
    from api.server import run_server
    from elastic.init_elasticsearch import create_index_and_fill_with_data

    if os.environ['SCRAP_WEBPAGE'] == 'True':
        # TODO Add Scrapping
        # Assumes that scarping returns csv in folder raw_data
        pass
    if os.environ['BUILD_ELASTIC'] == 'True':
        """
        Initializes Elasticsearch db with data
        Needs raw_data/books.csv and raw_data/users_and_books.csv files 
        """
        # Uncomment to convert csv to json and filter data
        # books_json_path = convert_csv_to_json(os.environ['PATH_TO_BOOKS'])
        # users_json_path = convert_users_csv_to_json(os.environ['PATH_TO_USERS'])
        create_index_and_fill_with_data('books_index', os.environ['PATH_TO_BOOKS'].replace(".csv", ".json"),
                                        'assets/books_index_def.json')
        create_index_and_fill_with_data('users_and_books',
                                        os.environ['PATH_TO_USERS'].replace(".csv",
                                                                            ".json"),
                                        'assets/users_and_books.json')
    if os.environ['RUN_SERVER'] == 'True':
        run_server()
