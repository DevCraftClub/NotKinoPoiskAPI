from typing import Optional

from requests import Session

from NotKinoPoiskAPI.Endpoint.NKPA import NKPA
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Responses.MediaPostsResponse import MediaPostsResponse


class KpMedia(NKPA):
	"""
	Класс для работы с сериалами и фильмами. Эндпоийнт /media_posts
	"""

	def __init__(self, api_key: Optional[str] = None, proxy: Optional[ProxyController] = None,
	             user_agent: Optional[str] = None,
	             headers: Optional[dict] = None,
	             session: Optional[Session] = None, cache_path: Optional[str] = None, timeout: int = 5):
		"""
		Конструктор класса

		Args:
			api_key (Optional[str]): API-Key для подключения
			proxy (Optional[ProxyController]): Прокси для подключения
			session (Optional[Session]): Сессия для запросов
			user_agent (Optional[str]): User-Agent для запросов
			headers (Optional[dict]): Дополнительные заголовки
			timeout (int): Время ожидания ответа
			cache_path (Optional[str]): Путь к папке кеша
		"""
		super().__init__(api_key=api_key, proxy=proxy, user_agent=user_agent, headers=headers, session=session,
		                 cache_path=cache_path, timeout=timeout)

	def get_posts(self, page: int = 1) -> MediaPostsResponse:
		"""
		Метод для получения медиа новостей с кинопоиска

		**Endpoint**: /api/v1/media_posts

		Args:
			page (int): Номер страницы

		Returns:
			MediaPostsResponse: Медиа новости
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url('media_posts', '1', page=page)),
		                                       MediaPostsResponse)
