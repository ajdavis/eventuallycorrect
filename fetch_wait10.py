import unittest

from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


class MyTestCase(unittest.TestCase):
    def test_http_fetch(self):
        io_loop = IOLoop.instance()
        client = AsyncHTTPClient(io_loop=io_loop)

        def callback(response):
            self.assertEqual(200, response.code)
            io_loop.stop()

        client.fetch("http://nsa.gov",
                     callback=callback)

        io_loop.start()
