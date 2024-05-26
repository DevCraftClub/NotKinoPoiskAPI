from typing import Optional

from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Profession import Profession


@dataclass
class PersonResponseFilms:
	"""
	Класс для хранения краткой информации о фильме в списке сотрудника.
	:param filmId: ID фильма или сериала
	:param nameRu: русское название
	:param nameEn: английское название
	:param rating: описание рейтинга
	:param general: основное состав
	:param description: описание роли в съёмках
	:param professionKey: ключ роли в съёмках
	"""
	filmId: int
	nameRu: Optional[str]
	nameEn: Optional[str]
	rating: Optional[str]
	general: bool
	description: Optional[str]
	professionKey: Optional[Profession]

	def __post_init__(self):
		if self.professionKey is not None and isinstance(self.professionKey, str):
			self.professionKey = ObjectController.find_enum(self.professionKey, Profession)

	def __str__(self):
		"""
		Выводит отформатировано название фильма.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
