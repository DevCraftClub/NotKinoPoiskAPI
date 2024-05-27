from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class AwardPerson:
	"""
	Класс для хранения информации о награжденном.
	"""
	kinopoiskId: int
	"""Уникальный идентификатор"""
	webUrl: str
	"""Ссылка на страницу"""
	nameRu: Optional[str]
	"""Имя на русском языке"""
	nameEn: Optional[str]
	"""Имя на английском языке"""
	sex: Sex
	"""Пол"""
	posterUrl: str
	"""Ссылка на изображение"""
	growth: Optional[int]
	"""Рост"""
	birthday: Optional[str]
	"""Дата рождения"""
	death: Optional[str]
	"""Дата смерти"""
	age: Optional[int]
	"""Возраст"""
	birthplace: Optional[str]
	"""Место рождения"""
	deathplace: Optional[str]
	"""Место смерти"""
	profession: Optional[str]
	"""Профессия"""

	def __post_init__(self):
		if isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)
