import time
import unittest

from tornado.ioloop import IOLoop

from my_application import delay_async


class MyTestCase(unittest.TestCase):
    def test_sleep(self):
        start = time.time()
        io_loop = IOLoop.instance()

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)
            io_loop.stop()

        delay_async(1, done)
        io_loop.start()
