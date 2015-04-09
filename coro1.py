import logging

from motor import MotorClient
from tornado import testing


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        logging.getLogger('tornado').setLevel(logging.CRITICAL)
        self.client = MotorClient()

    def test_find_one(self):
        collection = self.client.test.collection
        document = yield collection.find_one({'_id': 1})
        self.assertEqual({'_id': 1, 'key': 'value'}, document)
