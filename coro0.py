import unittest

from pymongo import MongoClient


class MyTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.client = MongoClient()

        collection = self.client.test.collection
        collection.remove()
        collection.insert({'_id': 0})
        collection.insert({'_id': 1, 'key': 'value'})
        collection.insert({'_id': 2})

    def test_find_one(self):
        collection = self.client.test.collection
        document = collection.find_one({'_id': 1})
        self.assertEqual({'_id': 1, 'key': 'value'}, document)
