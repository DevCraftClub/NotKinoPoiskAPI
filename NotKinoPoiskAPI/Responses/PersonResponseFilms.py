from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Profession import Profession


@dataclass
class PersonResponseFilms:
	"""
	Класс для хранения краткой информации о фильме в списке сотрудника.
	"""
	filmId: int
	"""ID фильма или сериала"""
	nameRu: Optional[str]
	"""русское название"""
	nameEn: Optional[str]
	"""английское название"""
	rating: Optional[str]
	"""описание рейтинга"""
	general: bool
	"""основной состав"""
	description: Optional[str]
	"""описание роли в съёмках"""
	professionKey: Optional[Profession]
	"""ключ роли в съёмках"""

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
