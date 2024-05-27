from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.FactType import FactType


@dataclass
class Fact:
	"""
	Класс для хранения информации о факте.
	"""
	text: str
	"""Описание факта"""
	type: FactType
	"""Тип"""
	spoiler: bool = False
	"""Спойлер"""

	def __post_init__(self):
		if self.type is not None and isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, FactType)
