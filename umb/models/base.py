# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from .. import utils

class Base(object):
	
	def __init__(self, arg):
		pass

	@classmethod
	def new_from_json_dict(cls, data):
		new_data = {utils.to_snake_case(key): value
					for key, value in data.items()}

		return cls(**new_data)

	@staticmethod
	def get_or_new_from_json_dict(data, cls):
		if isinstance(data, cls):
			return data
		elif isinstance(data, dict):
			return cls.new_from_json_dict(data)

		return None