# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from abc import ABCMeta
from future.utils import with_metaclass

class base_error(with_metaclass(ABCMeta, Exception)):
	def __init__(self, message='-'):
		self.message = message

	def __repr__(self):
		return str(self)

	def __str__(self):
		return '<{0} [{1}]>'.format(
			self.__class__.__name__, self.message)

class UMBApiError(base_error):
	def __init__(self, status_code, error=None):
		super(UMBApiError, self).__init__(error)

		self.status_code = status_code
		self.error = error

	def __str__(self):
		return '{0}: status_code={1}, error_response={2}'.format(
			self.__class__.__name__, self.status_code, self.error)