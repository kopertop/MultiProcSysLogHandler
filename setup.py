#!/usr/bin/env python

# Copyright (c) 2014, Chris Moyer <cmoyer@newstex.com>
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# 'Software'), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from mpSyslogHandler import __version__

setup(name = 'mpSyslogHandler',
	version = __version__,
	description = 'MultiProcess-safe SysLog Handler',
	author = 'Chris Moyer',
	author_email = 'cmoyer@newstex.com',
	url = 'https://github.com/kopertop/MultiProcSysLogHandler',
	packages = ['mpSyslogHandler'],
	license = 'MIT',
	platforms = 'Posix; MacOS X; Windows',
	classifiers = ['Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Topic :: Software Development',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7'],
	)
