How to use
----------------

The following examples assume a log format of 
    
    ``[%(name)s - %(level)s] %(message)s``

You may want to read the :ref:`survival` to achieve this.

Quick, log once
::::::::::::::::


Say you're in ``myapp/models/music.py``

.. code-block:: python

    import quicklogging
    quicklogging.error("Hello world")

Your output will be::

    [myapp.models.music - ERROR] Hello world

Log twice
:::::::::

Actually you're logging more than once in ``myapp/views/music.py`` and want to optimize:

.. code-block:: python

    import quicklogging
    logger = quicklogging.get_logger()
    logger.debug("Howdy?")

This produces::

    [myapp.views.music - DEBUG] Howdy?

then, 

.. code-block:: python

    logger.warning("plop")

produces::

    [myapp.views.music - WARNING] plop

