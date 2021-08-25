import csv
import glob
import json
import logging
import os
import sys

import pandas as pd

from process_data.string_filter import filter_book_name, remove_special_chars
from search.main_search_engine import find_book_id_by_book_name


# Needs to overcome the built in limit in csv library
def change_max_size_limit_csv():
    max_int = sys.maxsize
    while True:
        # decrease the max_int value by factor 10
        # as long as the OverflowError occurs.

        try:
            csv.field_size_limit(max_int)
            break
        except OverflowError:
            max_int = int(max_int / 10)


change_max_size_limit_csv()


def convert_csv_to_json(csv_file_path):
    data = {}
    with open(csv_file_path, encoding='utf-8-sig') as csvf:
        csv_reader = csv.DictReader(csvf)
        for index, row in enumerate(csv_reader):
            row = {k: remove_special_chars(v) for k, v in row.items()}
            row['book_name'] = filter_book_name(row['book_name'])
            if row['book_name'] not in data:
                data[row['book_name']] = row
    # Filter data to be unique
    data = list(data.values())

    new_path = csv_file_path.replace(".csv", ".json")
    with open(new_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    return new_path


def combine_csv():
    file_extension = '.csv'
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    prev_dir_name = os.getcwd()
    os.chdir(dir_name + r"\\out")
    all_filenames = [i for i in glob.glob(f"*{file_extension}")]
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

    # Take back dir state
    os.chdir(prev_dir_name)

    # export to csv
    combined_csv.to_csv("data/data.csv",
                        index=False, encoding='utf-8-sig')


def convert_users_csv_to_json(path_to_users_csv='raw_data/users_and_books.csv'):
    data = []
    user_id = 0
    prev_user_number = -1
    with open(path_to_users_csv, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for index, row in enumerate(csv_reader):
            book_id = find_book_id_by_book_name(row['book_name'])
            if book_id:
                if prev_user_number != row['user_id']:
                    user_id += 1
                    prev_user_number = row['user_id']
                to_append = {
                    'user_id': str(user_id),
                    'book_id': book_id
                }
                data.append(to_append)
                logging.info('Added book and user!', user_id, book_id)
    logging.info("Finished: user_id", user_id)
    new_path = path_to_users_csv.replace(".csv", ".json")
    with open(new_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    return new_path
