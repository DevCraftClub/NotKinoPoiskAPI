from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.PersonByNameResponseItem import PersonByNameResponseItem


@dataclass
class PersonByNameResponse(GeneralResponse):
	"""
	Класс для хранения информации о персоне по имени.
	"""
	items: List[PersonByNameResponseItem] = field(default_factory=list)
	"""Список персон"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, PersonByNameResponseItem)

	def add_items(self, items: Union[PersonByNameResponseItem, list[PersonByNameResponseItem]]):
		"""
		Добавление персон

		:param Union[PersonByNameResponseItem, list[PersonByNameResponseItem]] items: Персона или список персон
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
