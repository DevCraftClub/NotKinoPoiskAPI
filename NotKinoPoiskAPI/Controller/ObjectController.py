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

		Args:
			json_data (Union[str, Dict]): Данные в формате json
			object_type (Any): Тип объекта

		Returns:
			Any: Объект
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

		Args:
			items (List): Список данных в формате json
			object_data (Any): Тип объекта

		Returns:
			List[Any]: Список объектов
		"""
		return [ObjectController.json_to_object(item, object_data) for item in items]

	@staticmethod
	def find_enum(enum_data: str, enum_obj: Any):
		"""
		Поиск элемента в Enum и возвращает объект Enum

		Args:
			enum_data (str): Имя элемента
			enum_obj (Any): Enum

		Returns:
			Any: Элемент Enum
		"""
		for e in enum_obj:
			if e.name == enum_data:
				return e
		return None
