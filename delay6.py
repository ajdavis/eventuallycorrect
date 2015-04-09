import time

from tornado import testing

from my_application import delay_async


class MyTestCase(testing.AsyncTestCase):
    def test_delay(self):
        start = time.time()
        delay_async(1, callback=self.stop)
        self.wait()
        duration = time.time() - start
        self.assertAlmostEqual(duration, 1, places=2)
