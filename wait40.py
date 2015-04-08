import time
import unittest

from tornado.ioloop import IOLoop
from tornado.stack_context import ExceptionStackContext

from my_application import delay_async


class MyTestCase(unittest.TestCase):
    def test_delay(self):
        start = time.time()
        io_loop = IOLoop.instance()

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)
            io_loop.stop()

        self.failure = None

        def handle_exception(typ, value, tb):
            io_loop.stop()
            self.failure = typ, value, tb

        with ExceptionStackContext(handle_exception):
            delay_async(start + 1, callback=done)

        io_loop.start()
        if self.failure:
            fail_typ, fail_value, fail_tb = self.failure
            raise fail_value
