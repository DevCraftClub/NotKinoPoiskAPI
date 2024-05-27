from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Profession import Profession


@dataclass
class StaffResponse:
	"""
	Объект участников съёмок фильма или сериала. Данные выводятся в виде списка.
	"""
	staffId: int
	"""Уникальный идентификатор сотрудника"""
	nameRu: Optional[str]
	"""Имя сотрудника на русском языке"""
	nameEn: Optional[str]
	"""Имя на английском языке"""
	description: Optional[str]
	"""Описание сотрудника"""
	posterUrl: str
	"""Фото сотрудника"""
	professionText: str
	"""Роль в съёмках"""
	professionKey: Profession
	"""Ключ роли в съёмках"""

	def __post_init__(self):
		if isinstance(self.professionKey, str):
			self.professionText = ObjectController.find_enum(self.professionKey, Profession)

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
