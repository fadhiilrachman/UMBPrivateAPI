# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import Base

class Error(Base):
	def __init__(self, message=None, details=None, **kwargs):
		super(Error, self).__init__(**kwargs)
		
		self.message = message

		new_details = []
		if details:
			for detail in details:
				new_details.append(
					self.get_or_new_from_json_dict(detail, ErrorDetail)
				)
		self.details = new_details

class ErrorDetail(Base):
	def __init__(self, message=None, property=None, **kwargs):
		super(ErrorDetail, self).__init__(**kwargs)

		self.message = message
		self.property = property