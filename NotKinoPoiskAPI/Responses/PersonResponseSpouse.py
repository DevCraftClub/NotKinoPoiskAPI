from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonResponseSpouse:
	"""
	Объект супруга / супруги сотрудника
	"""
	personId: int
	"""Уникальный идентификатор супруга"""
	name: Optional[str]
	"""Имя супруга"""
	divorced: bool
	"""Указывает на то, что супруги разведены"""
	divorcedReason: Optional[str]
	"""Причина развода"""
	sex: Optional[Sex]
	"""Пол супруга"""
	children: int
	"""Количество детей"""
	webUrl: str
	"""Ссылка на персону"""
	relation: str
	"""Описание отношения"""

	def __post_init__(self):
		if self.sex is not None and isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)

	def __str__(self):
		"""
		Выводит отформатировано имя супруга / супруги
		"""

		return self.name
