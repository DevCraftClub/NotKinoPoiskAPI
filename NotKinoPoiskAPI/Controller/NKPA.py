import random
from dataclasses import dataclass
from typing import Any, Optional
from urllib.parse import urlencode

from decouple import config
from requests import Session

from NotKinoPoiskAPI.Controller.Connector import Connector
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Responses.ApiKeyResponse import ApiKeyResponse


@dataclass
class NKPA:
	"""
	Класс работы с самим  Kinopoisk API Unofficial
	"""
	api_key: str
	session: Optional[Connector]
	api_link: str = 'https://kinopoiskapiunofficial.tech/api'

	def __init__(self, api_key: Optional[str] = None, proxy: Optional[ProxyController] = None, user_agent: Optional[str] = None,
				 headers: Optional[dict] = None,
				 session: Optional[Session] = None, timeout: int = 5):
		if api_key is None:
			api_keys_config = config('NKPA_API_KEY', default=None, cast=str)
			if api_keys_config is None:
				raise ValueError("API ключ не указан")
			api_key = random.choice(api_keys_config.split('||'))
		self.api_key = api_key
		self.session = Connector(api_key, proxy, session, user_agent, headers, timeout)

	def get_api_url(self, method: str, version: str = '2.2', **query) -> str:
		"""
		Метод для получения ссылки на метод API.
		:param version: Версия API.
		:param method: Метод API.
		:return str
		"""
		filtered_query = {k: v for k, v in query.items() if v is not None}
		query.clear()
		query.update(filtered_query)
		url_query = f'?{urlencode(query)}' if query is not None and len(query) > 0 else ''
		return f"{self.api_link}/v{version}/{method}{url_query}"

	def get_data(self, link: str) -> Any:
		"""
		Метод для отправки запроса с проверкой по квоте
		:param link: Ссылка на метод API.
		:return Any
		"""
		if self.get_api_info():
			return self.session.send(link)

	def get_api_info(self) -> bool:
		"""
		Метод для получения информации о ключе
		/api/v1/api_keys/{apiKey}
		:return bool
		TODO: Добавить кеш для проверки API ключа
		"""
		url = self.get_api_url(f'api_keys/{self.api_key}', '1')
		data: ApiKeyResponse
		data = self.session.send(url)
		if data.dailyQuota.used > data.dailyQuota.value:
			raise ValueError(f"Превышен лимит запросов\nИспользованный ключ: {self.api_key}")
		else:
			return True
