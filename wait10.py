import time
import unittest

from my_application import delay_async


class MyTestCase(unittest.TestCase):
    def test_sleep(self):
        start = time.time()
        delay_async(1, callback=)  # What goes here?
        duration = time.time() - start
        self.assertAlmostEqual(duration, 1, places=2)
