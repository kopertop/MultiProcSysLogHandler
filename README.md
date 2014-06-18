Multi-Processing safe SysLog Handler
------------------------------------

This logger is designed to be safe for Multi-Processing environments. It works just like a normal
SysLogHandler, except that it is safe to be used by applications that use the multiprocessing module
