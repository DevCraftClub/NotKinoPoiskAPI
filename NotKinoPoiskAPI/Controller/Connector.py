import random
from dataclasses import dataclass, field
from typing import Optional

import requests
from decouple import config
from requests import Session

from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Errors.ApiError import ApiError
from NotKinoPoiskAPI.Types.ProxyItem import ProxyItem


@dataclass
class Connector:
	"""
	Класс для подключения к API.
	:param proxy: Прокси для подключения.
	:param session: Сессия для запросов.
	:param user_agent: User-Agent для запросов.
	:param headers: Дополнительные заголовки.
	:param method: Метод запроса.
	:param timeout: Время ожидания ответа.
	"""
	api_key: str
	proxy: Optional[ProxyItem]
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
		if not self.session:
			self.session = Session()
		self.session.headers.update(self.headers)
		self.session.headers.update({
			'X-API-KEY': self.api_key,
			'Content-Type': 'application/json',
		})

		self.set_proxy()
		self.set_user_agent()

	def set_proxy(self):
		"""
		Установка прокси.
		"""
		proxy = self.proxy if self.proxy else ProxyController()
		if proxy:
			proxy_dict = {proxy.type.value: str(proxy)}
			try:
				requests.get('https://httpbin.org/headers?json', proxies=proxy_dict, timeout=5, verify=False)
			except Exception as e:
				raise Exception(f"Прокси недоступны: {e}.\nИспользованные прокси: {str(proxy)}")
			self.session.proxies = proxy_dict

	def set_user_agent(self):
		"""
		Установка User-Agent.
		"""
		user_agent_env = config.get('NKPA_USER_AGENT', default=None, cast=str)
		if user_agent_env:
			user_agents = user_agent_env.split('||')
			self.user_agent = random.choice(user_agents)
			self.session.headers.update({'User-Agent': self.user_agent})

	def send(self, url: str, params: dict = None, data: dict = None, json: dict = None, method: str = 'GET'):
		"""
		Отправка запроса.
		:param url: URL запроса.
		:param params: Параметры запроса.
		:param data: Данные запроса.
		:param json: JSON данные запроса.
		:param method: Метод запроса.
		"""

		try:
			response = self.session.request(method=method, url=url, params=params, data=data, json=json, timeout=self.timeout)

			if response.status_code != 200:
				raise Exception(f"Ошибка: {response.status_code}.\nОписание: {ApiError.get_error_description(response.status_code)}")

			return response.json()
		except Exception as e:
			raise Exception(f"Произошла ошибка: {e}")
