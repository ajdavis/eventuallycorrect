import unittest

from tornado.httpclient import AsyncHTTPClient


class MyTestCase(unittest.TestCase):
    def test_http_fetch(self):
        client = AsyncHTTPClient()
        client.fetch("http://www.tornadoweb.org",
                     callback=)  # <- what goes here?

        # Now what?
