import time
import unittest

from tornado.ioloop import IOLoop


class MyTestCase(unittest.TestCase):
    def test_sleep(self):
        start = time.time()
        io_loop = IOLoop.instance()
        durations = []

        def done1():
            durations.append(time.time() - start)

        def done2():
            durations.append(time.time() - start)
            io_loop.stop()

        io_loop.add_timeout(start + 1, callback=done1)
        io_loop.add_timeout(start + 2, callback=done2)
        io_loop.start()
        self.assertAlmostEqual(durations[0], 1, places=2)
        self.assertAlmostEqual(durations[1], 2, places=2)
