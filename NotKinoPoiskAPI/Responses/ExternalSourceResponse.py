from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ExternalSourceResponseItem import ExternalSourceResponseItem


@dataclass
class ExternalSourceResponse(GeneralResponse):
	"""
	Класс для хранения информации о внешних источниках.
	"""
	items: List[ExternalSourceResponseItem] = field(default_factory=list)
	"""Список найденных источников"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, ExternalSourceResponseItem)

	def add_items(self, items: Union[ExternalSourceResponseItem, list[ExternalSourceResponseItem]]):
		"""
		Добавление источников

		:param Union[ExternalSourceResponseItem, list[ExternalSourceResponseItem]] items: Источник или список источников
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
