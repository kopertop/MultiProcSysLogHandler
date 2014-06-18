"""
@Author: Chris Moyer <cmoyer@newstex.com>
@See: http://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python

Multi-Processing Syslog handler,
because the Syslog handler does not handle MultiProcessing
very well, this overrides the Syslog handler and makes sure
the emit function is called properly

"""
__version__ = '0.1.2'

from logging.handlers import SysLogHandler
import multiprocessing, threading, sys, traceback, socket

class MultiProcessingLog(SysLogHandler):
	"""A special SysLog MultiProcessing handler, which
	allows us to make SysLog work with multiple processes
	calling the log function at once"""

	def __init__(self,*args, **kwargs):
		SysLogHandler.__init__(self,*args, **kwargs)
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
				# This is taken directly from the SysLog Handler, but for some reason
				# when you call emit() from here instead of doing it in this function,
				# the resulting Syslog lines are still incorrect and contain <level>
				# in the output
				msg = self.format(record) + '\000'
				prio = '<%d>' % self.encodePriority(self.facility, self.mapPriority(record.levelname))
				# Message is a string. Convert to bytes as required by RFC 5424
				if type(msg) is unicode:
					msg = msg.encode('utf-8')
				msg = prio + msg
				try:
					self.socket.send(msg)
				except socket.error:
					self.socket.close() # See issue 17981
					self._connect_unixsocket(self.address)
					self.socket.send(msg)
			except (KeyboardInterrupt, SystemExit):
				raise
			except EOFError:
				break
			except:
				traceback.print_exc(file=sys.stderr)
				self.handleError(record)

	def send(self, s):
		self.queue.put_nowait(s)

	def _format_record(self, record):
		"""ensure that exc_info and args
		have been stringified.	Removes any chance of
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
