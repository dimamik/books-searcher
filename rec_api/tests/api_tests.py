import json
import unittest
from time import sleep

import config


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        # Setting up environment to test app
        # Elasticsearch needs to be running and filled with data
        config.set_env('ELASTIC_HOST', 'localhost')
        from wsgi import app
        app.testing = True
        self.app = app.test_client()
        self.first_book_example_id: str = 'VsljeHsBJbzFcSZZGGcj'
        self.second_book_example_id: str = 'XcljeHsBJbzFcSZZGGcj'

        self.user_id: str = "2050"

    def test_register_user(self):
        result = self.app.post(f'record/?book_id={self.first_book_example_id}')
        self.assertTrue(json.loads(result.data)['success'])
        self.user_id = json.loads(result.data)['user_id']
        self.assertIsInstance(self.user_id, str)
        result = self.app.post(f'/record/?user_id={self.user_id}&book_id={self.second_book_example_id}')
        self.assertTrue(json.loads(result.data)['success'])
        sleep(0.5)
        result = self.app.get(f'/get_user_favourite/?user_id={self.user_id}')
        list_of_books_ids = [el['_id'] for el in json.loads(result.data)]
        self.assertTrue(self.second_book_example_id in list_of_books_ids)

    def doCleanups(self) -> None:
        self.app.delete(f'record/?user_id={self.user_id}&book_id={self.first_book_example_id}')
        self.app.delete(f'record/?user_id={self.user_id}&book_id={self.second_book_example_id}')
        pass
