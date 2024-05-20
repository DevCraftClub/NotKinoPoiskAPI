from typing import Optional

from NotKinoPoiskAPI.Enums.Sex import Sex


class Spouse:
	"""
	Объект супруга / супруги сотрудника
	"""
	personId: Optional[int]
	name: Optional[str]
	divorced: bool = False
	divorcedReason: Optional[str]
	sex: Optional[Sex]
	children: int = 0
	webUrl: Optional[str]
	relation: Optional[str]

	def __init__(self, personId: Optional[int] = None, name: Optional[str] = None, divorced: bool = False,
				 divorcedReason: Optional[str] = None, sex: Optional[Sex] = None, children: int = 0,
				 webUrl: Optional[str] = None, relation: Optional[str] = None):
		"""
		Инициализация объекта супруга / супруги сотрудника
		:param personId: Optional[int] - Универсальный ID .
		:param name: Optional[str] - Имя
		:param divorced: bool - Указывает на то, что супруги разведены. По умолчанию: False.
		:param divorcedReason: Optional[str] - Причина развода.
		:param sex: Optional[Sex] - Пол супруга / супруги
		:param children: int - Количество детей
		:param webUrl: Optional[str] - Ссылка на персону
		:param relation: Optional[str] - Описание отношения
		"""
		self.personId = personId
		self.name = name
		self.divorced = divorced
		self.divorcedReason = divorcedReason
		self.sex = sex
		self.children = children
		self.webUrl = webUrl
		self.relation = relation

	def __str__(self):
		"""
		Выводит отформатировано имя супруга / супруги
		"""

		return self.name
