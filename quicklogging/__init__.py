"""
logging wrapper

Here lie only a few wrappers/tools, including those used by the app.ini config

Supplied convenience functions fetch a logger with the name of the module from
which you're calling them.
"""

import inspect
import logging


def get_logger(stackoverhead=0):
    """
    wrapper for getLogger

    Typical use, imaging you're in project/module/submodule.py:

    >>> l = get_logger()
    >>> l
    <logging.Logger at ... >
    >>> l.name
    project.module.submodule

    :param stackoverhead: defaults to 1. How deep to look in the stack for
        fetching the logger name.

    :rtype: logging.Logger

    .. note::
        this function may be expanded
    """
    frm = inspect.stack()[1 + stackoverhead]
    mod = inspect.getmodule(frm[0])

    if mod is None:
        basename = "<No module>"
    else:
        basename = mod.__name__

    return logging.getLogger(basename)


def _log_with_level(func_name, *args, **kwargs):
    stackoverhead = kwargs.pop('stackoverhead', 0)
    logger = get_logger(stackoverhead=stackoverhead + 1)
    logfunc = getattr(logger, func_name)
    logfunc(*args, **kwargs)


def debug(*args, **kwargs):
    _log_with_level('debug', stackoverhead=1, *args, **kwargs)


def info(*args, **kwargs):
    _log_with_level('info', stackoverhead=1, *args, **kwargs)


def warning(*args, **kwargs):
    _log_with_level('warning', stackoverhead=1, *args, **kwargs)


def error(*args, **kwargs):
    _log_with_level('error', stackoverhead=1, *args, **kwargs)


def critical(*args, **kwargs):
    _log_with_level('critical', stackoverhead=1, *args, **kwargs)


def exception(*args, **kwargs):
    _log_with_level('exception', stackoverhead=1, *args, **kwargs)
