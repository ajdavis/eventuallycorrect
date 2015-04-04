import unittest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


class MyTestCase(unittest.TestCase):
    def test_http_fetch(self):
        io_loop = IOLoop.instance()
        results = []
        client = AsyncHTTPClient(io_loop=io_loop)

        def callback(response):
            results.append(response)
            io_loop.stop()

        client.fetch("http://tornadoweb.org",
                     callback=callback)

        io_loop.start()
        response = results[0]
        self.assertEqual(200, response.code)

    def test_http_fetch2(self):
        io_loop = IOLoop.instance()
        results = []
        client = AsyncHTTPClient(io_loop=io_loop)

        def callback(response):
            results.append(response)
            io_loop.stop()

        client.fetch("http://tornadoweb.org",
                     callback=callback)

        io_loop.start()
        response = results[0]
        self.assertEqual(200, response.code)
