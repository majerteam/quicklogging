import contextlib
import logging
import six

import py.test


_LOGGING_CONFIGURED_STREAM = None


@py.test.fixture(scope="session")
def streamconfig():
    global _LOGGING_CONFIGURED_STREAM
    if not _LOGGING_CONFIGURED_STREAM:
        _LOGGING_CONFIGURED_STREAM = six.StringIO()
        logging.basicConfig(stream=_LOGGING_CONFIGURED_STREAM, level=logging.INFO)

    @contextlib.contextmanager
    def manager():
        _LOGGING_CONFIGURED_STREAM.truncate(0)  # reset stream
        _LOGGING_CONFIGURED_STREAM.seek(0)  # rewind stream
        yield _LOGGING_CONFIGURED_STREAM
        _LOGGING_CONFIGURED_STREAM.seek(0)  # rewind stream

    return manager


_STREAM = None


import collections
import quicklogging

class FakeStream:
    def __init__(self):
        self.buckets = collections.defaultdict(
            lambda: six.StringIO()
        )

    def write(self, buf):
        # This stack overhead computed by hand: this is the depth of the logging
        # module
        bucket = quicklogging.get_logger(stackoverhead=10).name
        if not buf.strip():
            if '\n' not in buf:
                return 0
            buf = '\n'
        output = self.buckets[bucket]
        result = output.write(buf)
        output.flush()
        return result

    def data(self, module_name):
        bucket = self.buckets[module_name]
        bucket.flush()
        bucket.seek(0)
        return bucket.read()

    def debug_buckets(self):
        return [
            (name, self.data(name))
            for name in self.buckets
        ]


def add_and_fetch_stream(loggername):
    global _STREAM
    if _STREAM is None:
        _STREAM = FakeStream()
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler(_STREAM)
    handler.setFormatter(
        logging.Formatter("%(levelname)s:%(name)s:%(lineno)s:%(message)s")
    )
    logger.addHandler(handler)
    return _STREAM
