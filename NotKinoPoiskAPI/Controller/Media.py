from typing import Optional, Any

from requests import Session

from NotKinoPoiskAPI.Controller.NKPA import NKPA
from NotKinoPoiskAPI.Responses.MediaPostsResponse import MediaPostsResponse


class Media(NKPA):
	"""
	Класс для работы с сериалами и фильмами. Эндпоийнт /media_posts
	"""

	def __init__(api_key: Optional[str] = None, proxy: Optional[Any] = None, user_agent: Optional[str] = None,
                 headers: Optional[dict] = None,
                 session: Optional[Session] = None, timeout: int = 5):
		super().__init__(api_key, proxy, user_agent, headers, session, timeout)

	def get_posts(self, page: int = 1) -> MediaPostsResponse:
		"""
		Метод для получения медиа новостей с кинопоиска
		/api/v1/media_posts
		:param page: Номер страницы.
		:return MediaPostsResponse
		"""
		return self.get_data(self.get_api_url('media_posts', '1', page=page))
