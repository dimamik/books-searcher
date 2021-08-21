from scrap.load_data_to_elastic import create_index_and_bulk_add_json
from services.server import run_server
from scrap.parse_litmir import make_readable_json
import json
import requests
import os
import logging
from config import init_config

init_config()


def create_index():
    # First create index in elastic_search_database
    with open('assets/post_req.json', "r") as json_file:
        data = json.load(json_file)
    url = f"http://localhost:9200/{os.environ['INDEX_NAME']}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        logging.info("Index successfully created")
    else:
        logging.error("Problems creating index...")


def init_elasticsearch():
    create_index()
    make_readable_json()
    create_index_and_bulk_add_json(
        f"{os.environ['INDEX_NAME']}", 'data/data.json')


if __name__ == "__main__":
    if os.environ['BUILD_ELASTIC'] == "True":
        init_elasticsearch()
    run_server()
