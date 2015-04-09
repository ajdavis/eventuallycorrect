import time

from tornado import gen
from tornado.ioloop import IOLoop


def delay(seconds):
    time.sleep(seconds)


def delay_async(seconds, callback):
    IOLoop.current().add_timeout(time.time() + seconds, callback)


@gen.coroutine
def delay_coro(seconds):
    yield gen.sleep(seconds)
