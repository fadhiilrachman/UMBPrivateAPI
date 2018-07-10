# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod, abstractproperty

import requests, json
from future.utils import with_metaclass

class http_client(with_metaclass(ABCMeta)):
	
	DEFAULT_TIMEOUT = 5

	def __init__(self, timeout=DEFAULT_TIMEOUT):
		self.timeout = timeout

	def get(self, url, headers=None, params=None, stream=False, timeout=None):
		raise NotImplementedError

	def post(self, url, headers=None, data=None, timeout=None):
		raise NotImplementedError

class requests_http_client(http_client):

	def __init__(self, timeout=http_client.DEFAULT_TIMEOUT):
		super(requests_http_client, self).__init__(timeout)

	def get(self, url, headers=None, params=None, stream=False, timeout=None):
		if timeout is None:
			timeout = self.timeout

		response = requests.get(
			url, headers=headers, params=params, stream=stream, timeout=timeout
		)

		return requests_http_response(response)

	def post(self, url, headers=None, data=None, timeout=None):
		if timeout is None:
			timeout = self.timeout

		response = requests.post(
			url, headers=headers, data=data, timeout=timeout
		)

		return requests_http_response(response)

class http_response(with_metaclass(ABCMeta)):

	@abstractproperty
	def status_code(self):
		raise NotImplementedError

	@abstractproperty
	def headers(self):
		raise NotImplementedError

	@abstractproperty
	def text(self):
		raise NotImplementedError

	@abstractproperty
	def content(self):
		raise NotImplementedError

	@abstractproperty
	def json(self):
		raise NotImplementedError

	@abstractproperty
	def iter_content(self, chunk_size=1024, decode_unicode=False):
		raise NotImplementedError

class requests_http_response(http_response):
	
	def __init__(self, response):
		self.response = response
		
	@property
	def status_code(self):
		return self.response.status_code

	@property
	def headers(self):
		return self.response.headers

	@property
	def text(self):
		return self.response.text

	@property
	def content(self):
		return self.response.content

	@property
	def json(self):
		return self.response.json()

	def iter_content(self, chunk_size=1024, decode_unicode=False):
		return self.response.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode)