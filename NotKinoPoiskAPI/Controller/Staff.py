from typing import Optional, Any

from requests import Session

from NotKinoPoiskAPI.Controller.NKPA import NKPA
from NotKinoPoiskAPI.Responses.StaffResponse import StaffResponse


class KpStaff(NKPA):
	"""
	Класс для работы с сотрудниками фильмов и сериалов. Эндпоийнт /staff
	"""
	def __init__(api_key: Optional[str] = None, proxy: Optional[Any] = None, user_agent: Optional[str] = None,
				 headers: Optional[dict] = None,
				 session: Optional[Session] = None, timeout: int = 5):
		super().__init__(api_key, proxy, user_agent, headers, session, timeout)

	def get_staff(self, film_id: int) -> list[StaffResponse]:
		"""
		Метод для получения информации о сотрудниках фильма
		/api/v2.2/films/{id}/staff
		:param film_id: ID фильма.
		:return list[StaffResponse]
		"""
		return self.get_data(self.get_api_url('staff', '1', filmId=film_id))

	

