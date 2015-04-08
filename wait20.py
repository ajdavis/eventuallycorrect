import time
import unittest

from my_application import delay_async


class MyTestCase(unittest.TestCase):
    def test_delay(self):
        start = time.time()

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)

        delay_async(1, done)
