import importlib.abc
import six
import sys
import types

import py.test


@py.test.fixture(scope="module")
def output_stream():
    stream = six.StringIO()
    import logging
    logging.basicConfig(stream=stream)
    return stream


_MESSAGES = (
    "Hello world",
    "My hovercraft is full of eels",
    "49.3",
)
_MODULE_NAMES = (
    "tests.mountains",
    "tests.music.instruments.cymbal",
    "tests.music",
    "tests.discombobulate",
    "tests.music.instruments",
    "tests.mountains.ventoux",
)


@py.test.fixture(scope="function", params=_MESSAGES)
def message(request):
    return request.param


@py.test.fixture(scope="function", params=_MODULE_NAMES)
def module_name(request):
    return request.param


_DUMMY_MODULE_TEMPLATE = (
    "import quicklogging\n"
    "quicklogging.error('{message}')"
)


class DummyModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, name, src_code, *args, **kwargs):
        self._dummy_name = name
        self._src_code = src_code
        self._filename = '{}.py'.format(self._dummy_name.replace('.', '/'))

    def get_filename(self, path):
        return self._filename

    def get_data(self, path):
        return self._src_code.encode('utf-8')

    def create_module(self, spec):
        mod = types.ModuleType(self._dummy_name)
        mod.__file__ = self._filename
        sys.modules[mod.__name__] = mod
        return mod


def test_output(output_stream, module_name, message):

    output_stream.truncate(0)  # reset stream
    output_stream.seek(0)  # rewind stream

    dummy_code = _DUMMY_MODULE_TEMPLATE.format(message=message)
    loader = DummyModuleLoader(module_name, dummy_code)
    module = loader.create_module(None)
    loader.exec_module(module)

    output_stream.seek(0)  # rewind stream
    expected = "ERROR:{}:{}".format(module_name, message)
    found = output_stream.read().strip()

    assert found == expected
