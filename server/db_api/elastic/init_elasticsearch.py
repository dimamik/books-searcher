import json
import logging

import requests

from elastic.load_data_to_elastic import create_index_and_bulk_add_json


def _create_index(index_name, index_definition_path):
    # First create index in elastic_search_database
    # with open('assets/books_index_def.json', "r") as json_file:
    with open(index_definition_path, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    url = f"http://localhost:9200/{index_name}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        logging.info("Index successfully created")
    else:
        logging.error("Problems creating index...")


def create_index_and_fill_with_data(index_name, data_json_path, index_definition_path):
    _create_index(index_name, index_definition_path)
    create_index_and_bulk_add_json(
        f"{index_name}", data_json_path)
    logging.info(f'Index {index_name} is successfully filled with data')
