from typing import Optional, Any

from requests import Session

from NotKinoPoiskAPI.Controller.NKPA import NKPA
from NotKinoPoiskAPI.Responses.PersonByNameResponse import PersonByNameResponse
from NotKinoPoiskAPI.Responses.PersonResponse import PersonResponse
from NotKinoPoiskAPI.Responses.StaffResponse import StaffResponse


class KpStaff(NKPA):
	"""
	Класс для работы с сотрудниками фильмов и сериалов. Эндпоийнт /staff и /persons
	"""

	def __init__(api_key: Optional[str] = None, proxy: Optional[Any] = None, user_agent: Optional[str] = None,
				 headers: Optional[dict] = None,
				 session: Optional[Session] = None, timeout: int = 5):
		super().__init__(api_key, proxy, user_agent, headers, session, timeout)

	def get_film_staff(self, film_id: int) -> list[StaffResponse]:
		"""
		Метод для получения информации о сотрудниках фильма
		/api/v1/staff
		:param film_id: ID фильма.
		:return list[StaffResponse]
		"""
		return self.get_data(self.get_api_url('staff', '1', filmId=film_id))

	def get_staff(self, person_id: int) -> PersonResponse:
		"""
		Метод для получения информации о сотруднике
		/api/v1/staff/{id}
		:param person_id: ID сотрудника.
		:return PersonResponse
		"""
		return self.get_data(self.get_api_url(f'staff/{person_id}'))

	def get_persons(self, name: str) -> PersonByNameResponse:
		"""
		Метод для поиска сотрудника по имени
		/api/v1/persons
		:param name: Имя сотрудника.
		:return PersonByNameResponse
		"""
		return self.get_data(self.get_api_url('persons', '1', name=name))
