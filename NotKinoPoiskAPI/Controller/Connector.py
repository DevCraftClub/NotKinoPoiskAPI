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

	:param str api_key: API-Key для подключения.
	:param ProxyController proxy: Прокси для подключения.
	:param Session session: Сессия для запросов.
	:param str user_agent: User-Agent для запросов.
	:param dict headers: Дополнительные заголовки.
	:param int timeout: Время ожидания ответа.
	"""
	api_key: str
	"""API-Key для подключения"""
	proxy: Optional[ProxyController]
	session: Optional[Session]
	user_agent: Optional[str]
	headers: dict = field(default_factory=dict)
	timeout: int = 5

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

		:param str url: URL запроса.
		:param dict params: Параметры запроса.
		:param dict data: Данные запроса.
		:param dict json: JSON данные запроса.
		:param str method: Метод запроса.

		:return: Возвращает JSON объект в случае удачи. При ошибке выбрасывает её и останавливает скрипт

		:rtype: dict
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
