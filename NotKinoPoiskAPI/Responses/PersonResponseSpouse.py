from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Sex import Sex


@data
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
	personId: NonNull[int]
	name: Optional[str]
	divorced: NonNull[bool]
	divorcedReason: Optional[str]
	sex: Optional[Sex]
	children: NonNull[int]
	webUrl: NonNull[str]
	relation: NonNull[str]

	def __str__(self):
		"""
		Выводит отформатировано имя супруга / супруги
		"""

		return self.name
