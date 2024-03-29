My logging helper library
=========================

Quicklogging is intended for 2 purposes:

  * shrink the boilerplate I need before I can log something by a few bits,
  * without changing the body of source code, change quick and dirty ``print()``'ing scripts into
    enterprise class software that logs.

What quicklogging does
======================

Quicklogging provides you with handy loggers named after the current module.

.. code:: python

    import quicklogging
    my_logger = quicklogging.get_logger()

This allows for silencing or raising the logging level for a specific part or a
whole hierarchy of (sub-)packages (ie. folders, in Python's slang).

Quicklogging can handle legacy calls to ``print()`` . This means that the working code can stay
as-is and still get logged

.. code:: python

    import quicklogging

    # Catches prints in the current module
    quicklogging.catch_prints()

    # Catches prints everywhere in the Python process
    quicklogging.catch_prints(catch_all=True)

    # -> does not print to stdout anymore, but is logged.
    print("hello world")

What quicklogging does NOT
==========================

Quicklogging does not configure the logging formatting or output as this would
not save any line; here is a basic example for general purpose code: `Quick
survival guide with the logging module
<https://quicklogging.readthedocs.io/en/latest/logging_survival.html>`_.

Quicklogging quality
====================

Quicklogging is covered by a test suite and has been working for years for me, but I wouldn't promise there is no bug.

I have tried documenting the code but would welcome proofreading; the API may change after discussion.
