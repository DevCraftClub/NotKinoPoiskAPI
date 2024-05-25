from typing import Optional

from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonResponseSpouse:
	"""
	Объект супруга / супруги сотрудника
	:param personId: Optional[int] - Универсальный ID .
	:param name: Optional[str] - Имя
	:param divorced: bool - Указывает на то, что супруги разведены. По умолчанию: False.
	:param divorcedReason: Optional[str] - Причина развода.
	:param sex: Optional[Sex] - Пол супруга / супруги
	:param children: int - Количество детей
	:param webUrl: Optional[str] - Ссылка на персону
	:param relation: Optional[str] - Описание отношения
	"""
	personId: int
	name: Optional[str]
	divorced: bool
	divorcedReason: Optional[str]
	sex: Optional[Sex]
	children: int
	webUrl: str
	relation: str

	def __post_init__(self):
		if self.sex is not None and isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)

	def __str__(self):
		"""
		Выводит отформатировано имя супруга / супруги
		"""

		return self.name
