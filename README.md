Multi-Processing safe SysLog Handler
------------------------------------

This logger is designed to be safe for Multi-Processing environments. It works just like a normal
SysLogHandler, except that it is safe to be used by applications that use the multiprocessing module


Usage
=====

Add this to your logging config (or boto.cfg if you are using boto)

	[handler_syslog]
	formatter = syslog
	class = mpSyslogHandler.MultiProcessingLog
	args = ('/dev/log',handlers.SysLogHandler.LOG_USER)
	level = INFO
