# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .config import config
from .exceptions import UMBApiError
from .http_client import http_client, requests_http_client

from .models import (
	Error
)

class UMB(object):

	DEFAULT_API_ENDPOINT = config.api_endpoint
	
	def __init__(self, endpoint=DEFAULT_API_ENDPOINT,
					timeout=http_client.DEFAULT_TIMEOUT, http_client=requests_http_client):

		self.endpoint = endpoint
		self.headers = {
			'User-Agent': config.user_agent
		}
		
		if http_client:
			self.http_client = http_client(timeout=timeout)
		else:
			self.http_client = requests_http_client(timeout=timeout)

	def login(self, username, password, timeout=None):
		path = config.http_api_path['login']
		data = {
			'device': config.device,
			'username': username,
			'password': password
		}

		return self._post(
			path, data=data, timeout=timeout
		)

	def _get(self, path, params=None, headers=None, stream=False, timeout=None):
		url = self.endpoint + path

		if headers is None:
			headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		headers.update(self.headers)

		response = self.http_client.post(
			url, headers=headers, params=params, stream=stream, timeout=timeout
		)

		self.__check_error(response)
		return response

	def _post(self, path, data=None, headers=None, timeout=None):
		url = self.endpoint + path

		if headers is None:
			headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		headers.update(self.headers)

		response = self.http_client.post(
			url, headers=headers, data=data, timeout=timeout
		)

		self.__check_error(response)
		return response

	def __check_error(self, response):
		if 200 <= response.status_code < 300:
			if response.json['data'] is None:
				raise UMBApiError(response.json['system']['code'], response.json['system']['message'])
			else:
				pass
		else:
			error = Error.new_from_json_dict(response.json)
			raise UMBApiError(response.status_code, error)