from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonByNameResponseItem:
	"""
	Объект персоны
	"""
	kinopoiskId: int
	"""Идентификатор"""
	webUrl: str
	"""Ссылка на страницу персоны"""
	nameRu: Optional[str]
	"""Имя на русском"""
	nameEn: Optional[str]
	"""Имя на английском"""
	sex: Optional[Sex]
	"""Пол"""
	posterUrl: str
	"""Ссылка на постер"""

	def __post_init__(self):
		if self.sex is not None and isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)
