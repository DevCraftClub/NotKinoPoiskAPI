import random
from dataclasses import dataclass, field
from typing import Optional

import requests
from decouple import config
from requests import Session

from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Errors.ApiError import ApiError


@dataclass
class Connector:
	"""
	Класс для подключения к API.
	"""
	api_key: str
	"""API-Key для подключения"""
	proxy: Optional[ProxyController]
	"""Прокси для подключения"""
	session: Optional[Session]
	"""Сессия для запросов"""
	user_agent: Optional[str]
	"""User-Agent для запросов"""
	headers: dict = field(default_factory=dict)
	"""Дополнительные заголовки"""
	timeout: int = 5
	"""Время ожидания ответа"""

	def __post_init__(self):
		"""
		Пост-Инициализация класса.
		"""
		self.initialize_session()

	def initialize_session(self):
		"""
		Инициализация сессии.
		"""
		if not self.proxy or isinstance(self.proxy, str):
			self.proxy = None
		if not self.session:
			self.session = Session()
		if not self.headers:
			self.headers = {}
		self.session.headers.update(self.headers)
		self.session.headers.update({
				'X-API-KEY'   : self.api_key,
				'Content-Type': 'application/json',
		})

		self.set_proxy()
		self.set_user_agent()

	def set_proxy(self):
		"""
		Установка прокси.

		Raises:
			Exception: Если прокси недоступны.
		"""
		proxy = self.proxy if self.proxy else ProxyController()
		if proxy and len(proxy.get_proxy_list()) > 0:
			proxy_item = proxy.get_random_proxy()
			proxy_dict = {proxy_item.type.value: str(proxy_item)}
			try:
				requests.get('https://httpbin.org/headers?json', proxies=proxy_dict, timeout=5, verify=False)
			except Exception as e:
				raise Exception(f"Прокси недоступны: {e}.\nИспользованные прокси: {str(proxy_item)}")
			self.session.proxies = proxy_dict

	def set_user_agent(self):
		"""
		Установка User-Agent.
		"""
		user_agent_env = config('NKPA_USER_AGENT', default=None, cast=str)
		if user_agent_env:
			user_agents = user_agent_env.split('||')
			self.user_agent = random.choice(user_agents)
			self.session.headers.update({'User-Agent': self.user_agent})

	def send(self, url: str, params: dict = None, data: dict = None, json: dict = None, method: str = 'GET'):
		"""
		Отправка запроса.

		Args:
			url (str): URL запроса.
			params (Dict): Параметры запроса.
			data (Dict): Данные запроса.
			json (Dict): JSON данные запроса.
			method (str): Метод запроса.

		Returns:
			Dict: Возвращает JSON объект в случае удачи. При ошибке выбрасывает её и останавливает скрипт.

		Raises:
			Exception: Если подключение к API произошло неуспешно
		"""

		try:
			response = self.session.request(method=method, url=url, params=params, data=data, json=json,
			                                timeout=self.timeout)

			if response.status_code != 200:
				raise Exception(
						f"Ошибка: {response.status_code}.\nОписание: {ApiError.get_error_description(response.status_code)}")

			return response.json()
		except Exception as e:
			raise Exception(f"Произошла ошибка: {e}")
