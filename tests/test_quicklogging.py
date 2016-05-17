import re
import py.test

import stringimporter

from . import add_and_fetch_stream
from . import streamconfig


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


_TEST_OUTPUT_MODULE_TEMPLATE = (
    "import quicklogging\n"
    "quicklogging.error('{message}')\n"
    "\n"
    "def get_my_logger():\n"
    "    return quicklogging.get_logger()"
)


def test_output(streamconfig, module_name, message):
    loader, module = stringimporter.import_str(
        module_name,
        _TEST_OUTPUT_MODULE_TEMPLATE.format(message=message),
        exec_module=False,
        filename="/tmp/coin_{}.py".format(module_name)
    )

    with streamconfig() as stream:
        loader.exec_module(module)

    expected = "ERROR:{}:{}".format(module_name, message)
    found = stream.read().strip()

    assert found == expected

_TEST_CATCHPRINT_MODULE_TEMPLATE = (
    "import quicklogging\n"
    "def run_the_printing_function():\n"
    "    quicklogging.catch_prints(catch_all=False)\n"
    "    print('{message}')\n"
    "\n"
    "def get_my_logger():\n"
    "    my_logger = quicklogging.get_logger()\n"
    "    return my_logger.name, [(h.stream, h.stream.buckets) for h in my_logger.handlers]"
)


_CALL_COUNT=0


def test_catch_prints(streamconfig, module_name):
    global _CALL_COUNT

    _CALL_COUNT += 1
    module_name = module_name
    message = "bonjour depuis {}".format(module_name, _CALL_COUNT)
    message = message.strip()

    stream = add_and_fetch_stream(module_name)

    py_src = _TEST_CATCHPRINT_MODULE_TEMPLATE.format(
        message=message, module=module_name
    )
    loader, themodule = stringimporter.import_str(
        module_name,
        py_src,
        exec_module=False,
        filename="/tmp/coin_{}.py".format(_CALL_COUNT)
    )

    loader.exec_module(themodule)
    themodule.run_the_printing_function()

    expected_re = "INFO:{}:\d+:{}".format(module_name, message)
    found = stream.data(module_name).strip()

    assert re.match(expected_re, found)


def test_hierarchical_catch_print(streamconfig):
    data = (
                (
                    'parent',
                    (
                        "import quicklogging\n"
                        "print('this is lost')\n"
                        "quicklogging.catch_prints(include_children=True)"

                    )
                ),
                ('parent.child', "print('message seen by parent')"),
                ('unrelated', "print('message not intercepted')"),
        )

    for module_name, py_src in data:
        # it's always the same stream
        stream = add_and_fetch_stream(module_name)

    loaders_modules = []
    for module_name, py_src in data:
        loaders_modules.append(
            stringimporter.import_str(
                module_name, py_src, exec_module=False
            )
        )
    for loader, module in loaders_modules:
        loader.exec_module(module)

    assert stream.data('parent') == ""
    assert re.match(
        "INFO:parent.child:\d+:message seen by parent",
        stream.data('parent.child')
    )
    assert stream.data('unrelated') == ""
