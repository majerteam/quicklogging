import quicklogging

from . import streamconfig


def test_catch_prints(streamconfig):
    with streamconfig() as stream:
        quicklogging.catch_prints()
        print("hello world")
    expected = "hello world"
    found = stream.read().strip()

    assert found == expected
