from motor import MotorClient
from tornado import gen, testing
from tornado.testing import gen_test


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        self.client = MotorClient()
        self.io_loop.run_sync(self.setup_coro)

    @gen.coroutine
    def setup_coro(self):
        collection = self.client.test.collection
        yield collection.remove()
        yield collection.insert({'_id': 0})
        yield collection.insert({'_id': 1, 'key': 'value'})
        yield collection.insert({'_id': 2})

    @gen_test
    def test_find_one(self):
        collection = self.client.test.collection
        document = yield collection.find_one({'_id': 1})
        self.assertEqual({'_id': 1, 'key': 'value'}, document)
