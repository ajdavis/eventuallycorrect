import logging
import time

from tornado import testing


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        logging.getLogger('tornado').setLevel(logging.CRITICAL)

    def test_delay(self):
        start = time.time()
        io_loop = self.io_loop

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)
            self.stop()

        io_loop.add_timeout(start + 2, callback=done)
        self.wait()
