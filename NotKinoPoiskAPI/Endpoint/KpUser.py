from typing import Optional

from requests import Session

from NotKinoPoiskAPI.Endpoint.NKPA import NKPA
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Responses.KinopoiskUserVoteResponse import KinopoiskUserVoteResponse


class KpUser(NKPA):
	"""
	Класс для работы с Endpoint /kp_users с API неофициального кинопоиска
	"""

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
		"""
		super().__init__(api_key=api_key, proxy=proxy, user_agent=user_agent, headers=headers, session=session,
		                 cache_path=cache_path, timeout=timeout)

	def get_votes(self, user_id: int, page: int = 1) -> KinopoiskUserVoteResponse:
		"""
		Метод для получения рейтинга пользователя

		:Endpoint: /api/v1/kp_users/{id}/votes
		:param int page: Номер страницы
		:param int user_id: ID пользователя на сайте
		:return: Рейтинга пользователя
		:rtype: KinopoiskUserVoteResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'kp_users/{user_id}/votes', '1', page=page)), KinopoiskUserVoteResponse)
