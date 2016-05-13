.. _majerti: http://majerti.fr
.. _pyramid: http://docs.pylonsproject.org/projects/pyramid/
.. _boilerplate: https://en.wikipedia.org/wiki/Boilerplate_code
.. _logging: https://docs.python.org/3.5/library/logging.html

quicklogging
=============

A Python logging wrapper to remove a bit of logging boilerplate.

``quicklogging`` provides direct access a logger with a relevant name (the name is the name of the module making the call) - purpose of this functionality: it's then very easy to tweak the log levels or handlers of individual loggers (based on the caller module name).

Licence, original authors
---------------------------

* MIT (see file ``LICENCE`` ).
* authors: majerti_ - Feth AREZKI

How to use
----------------

Direct to the point
::::::::::::::::::::

.. note::

    Here we assume a log format of ``[%(name)s - %(level)s] %(message)s``

Say you're in ``myapp/models/music.py``:

.. code-block:: python

    import quicklogging

    quicklogging.error("Hello world")

.. code-block:: 

    [myapp.models.music - ERROR] Hello world

Or, if you're logging more than once in ``myapp/views/music.py`` and want to optimize:

.. code-block:: python

    import quicklogging

    logger = quicklogging.get_logger()

    logger.debug("Howdy?")
    logger.warning("plop")

.. code-block:: 

    [myapp.views.music - DEBUG] Howdy?
    [myapp.views.music - WARNING] plop

``quicklogging`` wraps 

.. _debug: https://docs.python.org/3/library/logging.html#logging.Logger.debug
.. _info: https://docs.python.org/3/library/logging.html#logging.Logger.info
.. _warning: https://docs.python.org/3/library/logging.html#logging.Logger.warning
.. _error: https://docs.python.org/3/library/logging.html#logging.Logger.error
.. _critical: https://docs.python.org/3/library/logging.html#logging.Logger.critical
.. _exception: https://docs.python.org/3/library/logging.html#logging.Logger.exception

* debug_
* info_
* warning_
* error_
* critical_
* exception_ 

(but before:) Initial config (boilerplate_)
:::::::::::::::::::::::::::::::::::::::::::::

Disclaimer: we are not responsible for the boilerplate logging API

You still need to configure logging somewhere at the start of your script -for complex apps (pyramid_ for example), initial scaffolding is likely to do this for you (see generated .ini file).

Example boilerplate_ for a script
...................................

Logging to ``my_app.log`` :

.. code-block:: python

    import logging
    import logging.handlers
    import quicklogging

    # basicConfig is only effective once (if the root logger was not configured before)
    logging.basicConfig(
        handlers=[logging.handlers.WatchedFileHandler('my_app.log')],
        format="%(asctime)s %(pathname)s:%(lineno)s%(message)s\\n",
        level=logging.WARNING
    )
