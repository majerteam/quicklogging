Task oriented doc
==========================================

.. Note:: 
    
    Many functions take a `stackoverhead` param, which is documented in :py:func:`quicklogging.base.get_logger`. 

Fetch a logger
---------------

Use :py:func:`quicklogging.base.get_logger` also available as :py:func:`quicklogging.get_logger`.

Then, you can use the logger normally.

Available log wrappers
-----------------------

If logging multiple times, it is slower to use these than to use :py:func:`quicklogging.get_logger` and log with received object.

    * :py:func:`quicklogging.debug`     →  :py:func:`logging.debug`    
    * :py:func:`quicklogging.info`      →  :py:func:`logging.info` 
    * :py:func:`quicklogging.warning`   →  :py:func:`logging.warning` 
    * :py:func:`quicklogging.error`     →  :py:func:`logging.error` 
    * :py:func:`quicklogging.critical`  →  :py:func:`logging.critical` 
    * :py:func:`quicklogging.exception` →  :py:func:`logging.exception`

print wrapping functionality
-----------------------------

``quicklogging`` provides

    * :py:func:`quicklogging.catch_prints`
    * :py:func:`quicklogging.warn_prints` 


