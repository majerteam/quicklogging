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
        logging.basicConfig(
            stream=_LOGGING_CONFIGURED_STREAM, level=logging.INFO
        )

    @contextlib.contextmanager
    def manager():
        _LOGGING_CONFIGURED_STREAM.truncate(0)  # reset stream
        _LOGGING_CONFIGURED_STREAM.seek(0)  # rewind stream
        yield _LOGGING_CONFIGURED_STREAM
        _LOGGING_CONFIGURED_STREAM.seek(0)  # rewind stream

    return manager


_MESSAGES = (
    "Hello world",
    "My hovercraft is full of eels",
    "49.3",
)


@py.test.fixture(scope="function", params=_MESSAGES)
def message(request):
    return request.param


_MODULE_NAMES = (
    "tests.mountains",
    "tests.music.instruments.cymbal",
    "tests.music",
    "tests.discombobulate",
    "tests.music.instruments",
    "tests.mountains.ventoux",
)


@py.test.fixture(scope="function", params=_MODULE_NAMES)
def module_name(request):
    return request.param
