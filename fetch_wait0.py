import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_http_fetch(self):
        response = requests.get("http://www.tornadoweb.org")
        self.assertEqual(200, response.status_code)
