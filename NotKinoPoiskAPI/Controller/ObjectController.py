import json
from types import SimpleNamespace
from typing import Any, Union, List


class ObjectController:

	@staticmethod
	def json_to_object(json_data: Union[str, dict], object_type: Any):
		if json_data is None:
			return None
		if isinstance(json_data, str):
			return json.loads(json_data, object_type=lambda d: SimpleNamespace(**d))
		return object_type(**json_data)

	@staticmethod
	def list_to_object(items: List, object_data: Any):
		return [ObjectController.json_to_object(item, object_data) for item in items]

	@staticmethod
	def find_enum(enum_data: str, enum_obj: Any):
		for e in enum_obj:
			if e.name == enum_data:
				return e
		return None