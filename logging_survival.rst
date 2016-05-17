.. _survival:

Annex: Quick survival guide with the logging module
====================================================

Sadly, some config still needs to take place for the :py:mod:`logging` module.

.. _pyramid: http://docs.pylonsproject.org/projects/pyramid/
.. _boilerplate: https://en.wikipedia.org/wiki/Boilerplate_code

Disclaimer: we are not responsible for the boilerplate_ required by the logging API

You still need to configure logging somewhere at the start of your script -for complex apps (pyramid_ for example), initial scaffolding is likely to do this for you (see generated .ini file).

Example boilerplate_ for a script logging to ``my_app.log``:

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
