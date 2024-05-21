from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Profession import Profession


@data
class PersonResponseFilms:
	"""
	Класс для хранения краткой информации о фильме в списке сотрудника.
	"""
	filmId: NonNull[int]
	nameRu: Optional[str]
	nameEn: Optional[str]
	rating: Optional[str]
	general: NonNull[bool]
	description: Optional[str]
	professionKey: Optional[Profession]

	def __init__(self, filmId: Optional[int] = None, nameRu: Optional[str] = None, nameEn: Optional[str] = None,
	             rating: Optional[str] = None, general: bool = False, description: Optional[str] = None,
	             professionKey: Optional[Profession] = None):
		"""
		:param filmId: ID фильма или сериала
		:param nameRu: русское название
		:param nameEn: английское название
		:param rating: описание рейтинга
		:param general: основное состав
		:param description: описание роли в съёмках
		:param professionKey: ключ роли в съёмках
		"""
		self.filmId = filmId
		self.nameRu = nameRu
		self.nameEn = nameEn
		self.rating = rating
		self.general = general
		self.description = description
		self.professionKey = professionKey

	def __str__(self):
		"""
		Выводит отформатировано название фильма.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu