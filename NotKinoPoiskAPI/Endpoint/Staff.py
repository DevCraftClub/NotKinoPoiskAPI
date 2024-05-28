from typing import List, Optional

from requests import Session

from NotKinoPoiskAPI.Endpoint.NKPA import NKPA
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Responses.PersonByNameResponse import PersonByNameResponse
from NotKinoPoiskAPI.Responses.PersonResponse import PersonResponse
from NotKinoPoiskAPI.Responses.StaffResponse import StaffResponse


class KpStaff(NKPA):
	"""
	Класс для работы с сотрудниками фильмов и сериалов. Эндпоийнт /staff и /persons
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

	def get_film_staff(self, film_id: int) -> List[StaffResponse]:
		"""
		Метод для получения информации о сотрудниках фильма

		**Endpoint**: /api/v1/staff

		Args:
			film_id (int): ID фильма

		Returns:
			List[StaffResponse]: Информация о сотрудниках фильма
		"""
		return ObjectController.list_to_object(self.get_data(self.get_api_url('staff', '1', filmId=film_id)),
		                                       StaffResponse)

	def get_staff(self, person_id: int) -> PersonResponse:
		"""
		Метод для получения информации о сотруднике

		**Endpoint**: /api/v1/staff/{id}

		Args:
			person_id (int): ID сотрудника

		Returns:
			PersonResponse: Информация о сотруднике
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'staff/{person_id}', '1')), PersonResponse)

	def get_persons(self, name: str) -> PersonByNameResponse:
		"""
		Метод для поиска сотрудника по имени

		**Endpoint**: /api/v1/persons

		Args:
			name (str): Имя сотрудника.

		Returns:
			PersonByNameResponse: Результат поиска
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url('persons', '1', name=name)),
		                                       PersonByNameResponse)
