from motor import MotorClient
from tornado import testing
from tornado.testing import gen_test


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        self.client = MotorClient()

    @gen_test
    def test_find_one(self):
        collection = self.client.test.collection
        document = yield collection.find_one({'_id': 1})
        self.assertEqual({'_id': 1, 'key': 'value'}, document)
