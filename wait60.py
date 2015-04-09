import logging
import time

from tornado import testing

from my_application import delay_async


class MyTestCase(testing.AsyncTestCase):
    def setUp(self):
        super().setUp()
        logging.getLogger('tornado').setLevel(logging.CRITICAL)

    def test_delay(self):
        start = time.time()

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)
            self.stop()

        delay_async(1, callback=done)
        self.wait()
