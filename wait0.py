import time
import unittest

from my_application import delay


class MyTestCase(unittest.TestCase):
    def test_sleep(self):
        start = time.time()
        delay(1)
        duration = time.time() - start
        self.assertAlmostEqual(duration, 1, places=2)
