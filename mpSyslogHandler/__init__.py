"""
@Author: Chris Moyer <cmoyer@newstex.com>
@See: http://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python

Multi-Processing Syslog handler,
because the Syslog handler does not handle MultiProcessing
very well, this overrides the Syslog handler and makes sure
the emit function is called properly

"""
from logging.handlers import SysLogHandler
import multiprocessing, threading, sys, traceback

class MultiProcessingLog(SysLogHandler):
	"""A special SysLog MultiProcessing handler, which
	allows us to make SysLog work with multiple processes
	calling the log function at once"""

	def __init__(self,*args, **kwargs):
		SysLogHandler.__init__(self, *args, **kwargs)
		self.queue = multiprocessing.Queue(-1)

		t = threading.Thread(target=self.receive)
		t.daemon = True
		t.start()

	def receive(self):
		while True:
			try:
				record = self.queue.get()
				if record is None:
					raise EOFError
				SysLogHandler.emit(self, record)
			except (KeyboardInterrupt, SystemExit):
				raise
			except EOFError:
				break
			except:
				traceback.print_exc(file=sys.stderr)

	def send(self, s):
		self.queue.put_nowait(s)

	def _format_record(self, record):
		"""ensure that exc_info and args
		have been stringified.  Removes any chance of
		unpickleable things inside and possibly reduces
		message size sent over the pipe"""
		if record.args:
			record.msg = record.msg % record.args
			record.args = None
		if record.exc_info:
			self.format(record)
			record.exc_info = None

		return record

	def emit(self, record):
		try:
			s = self._format_record(record)
			self.send(s)
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			self.handleError(record)

	def close(self):
		"""Close the loggers"""
		self.queue.put(None)
		SysLogHandler.close(self)
