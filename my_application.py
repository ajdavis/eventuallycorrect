import time
from tornado.ioloop import IOLoop


def delay(seconds):
    time.sleep(seconds)


def delay_async(seconds, callback, io_loop=None):
    if not io_loop:
        io_loop = IOLoop.instance()

    io_loop.add_timeout(time.time() + seconds, callback)
