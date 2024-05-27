import random
from dataclasses import dataclass
from typing import Any, Optional
from urllib.parse import urlencode

from decouple import config
from requests import Session

from NotKinoPoiskAPI.Controller.CacheController import CacheController
from NotKinoPoiskAPI.Controller.Connector import Connector
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Enums.ApiAccountType import ApiAccountType
from NotKinoPoiskAPI.Responses.ApiKeyResponse import ApiKeyResponse


@dataclass
class NKPA:
	"""
	Класс работы с самим  Kinopoisk API Unofficial
	"""
	api_key: str
	"""API ключ"""
	session: Optional[Connector]
	"""Сессия для запросов"""
	cache: Optional[CacheController]
	"""Кеш для запросов"""
	api_link: str = 'https://kinopoiskapiunofficial.tech/api'
	"""Ссылка на API"""

	def __init__(self, api_key: Optional[str] = None, proxy: Optional[ProxyController] = None,
	             user_agent: Optional[str] = None,
	             headers: Optional[dict] = None,
	             session: Optional[Session] = None, cache_path: Optional[str] = None, timeout: int = 5):
		"""
		Конструктор класса

		:param str api_key: API-Key для подключения.
		:param ProxyController proxy: Прокси для подключения.
		:param Session session: Сессия для запросов.
		:param str user_agent: User-Agent для запросов.
		:param dict headers: Дополнительные заголовки.
		:param int timeout: Время ожидания ответа.
		:param str cache_path: Путь к папке кеша.
		:raise ValueError: Если API ключ не указан.
		"""
		if api_key is None:
			api_keys_config = config('NKPA_API_KEY', default=None, cast=str)
			if api_keys_config is None:
				raise ValueError("API ключ не указан")
			api_key = random.choice(api_keys_config.split('||'))
		self.api_key = api_key
		self.session = Connector(api_key=api_key, proxy=proxy, session=session, user_agent=user_agent, headers=headers,
		                         timeout=timeout)
		self.cache = CacheController(cache_path)

	def get_api_url(self, method: str, version: str = '2.2', **query) -> str:
		"""
		Метод для получения ссылки на метод API. Фильтрует пустые (`None`) данные

		:param str version: Версия API.
		:param str method: Метод API.
		:param dict query: Параметры запроса.
		:return: Ссылка на метод API.
		:rtype: str
		"""
		filtered_query = {k: v for k, v in query.items() if v is not None}
		query.clear()
		query.update(filtered_query)
		url_query = f'?{urlencode(query)}' if query is not None and len(query) > 0 else ''
		return f"{self.api_link}/v{version}/{method}{url_query}"

	def get_data(self, link: str) -> dict:
		"""
		Запрашивает данные по эндпойнту, проверяя предварительно данные в кеше

		:param str link: Ссылка на метод API.
		:return: Данные по эндпойнту
		:rtype: dict
		"""
		if self.get_api_info():
			cache = self.cache.get_cache(link)
			if cache is not None:
				return cache
			else:
				data = self.session.send(link)
				self.cache.set_cache(link, data)

			return data

	def get_api_info(self) -> bool:
		"""
		Метод для получения информации о ключе

		:Endpoint: /api/v1/api_keys/{apiKey}
		:return: Возвращает либо утвердительный ответ, либо вызывает ошибку
		:rtype: bool
		:raise ValueError: Если превышен лимит запросов
		"""
		url = self.get_api_url(f'api_keys/{self.api_key}', '1')
		data = ObjectController.json_to_object(self.session.send(url), ApiKeyResponse)

		if data.accountType == ApiAccountType.UNLIMITED or data.dailyQuota.value == -1 or data.dailyQuota.used < data.dailyQuota.value:
			return True
		else:
			raise ValueError(f"Превышен лимит запросов\nИспользованный ключ: {self.api_key}")
