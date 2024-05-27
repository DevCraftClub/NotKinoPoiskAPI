import json
from types import SimpleNamespace
from typing import Any, List, Union


class ObjectController:
	"""
	Класс для работы с объектами
	"""
	@staticmethod
	def json_to_object(json_data: Union[str, dict], object_type: Any):
		"""
		Конвертация json в объект

		:param Union[str, dict] json_data: Данные в формате json
		:param Any object_type: Тип объекта
		:return: Объект
		:rtype: Any
		"""
		if json_data is None:
			return None
		if isinstance(json_data, str):
			return json.loads(json_data, object_type=lambda d: SimpleNamespace(**d))
		return object_type(**json_data)

	@staticmethod
	def list_to_object(items: List, object_data: Any):
		"""
		Конвертация списка json в список объектов

		:param List items: Список данных в формате json
		:param Any object_data: Тип объекта
		:return: Список объектов
		:rtype: List[Any]
		"""
		return [ObjectController.json_to_object(item, object_data) for item in items]

	@staticmethod
	def find_enum(enum_data: str, enum_obj: Any):
		"""
		Поиск элемента в Enum и возвращает объект Enum

		:param str enum_data: Имя элемента
		:param Any enum_obj: Enum
		:return: Элемент Enum
		:rtype: Any
		"""
		for e in enum_obj:
			if e.name == enum_data:
				return e
		return None
