from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ExternalSourceResponseItem import ExternalSourceResponseItem


@dataclass
class ExternalSourceResponse(GeneralResponse):
	"""
	Класс для хранения информации о внешних источниках.
	"""
	items: list[ExternalSourceResponseItem] = field(default_factory=list)

	def add_items(self, items: Union[ExternalSourceResponseItem, list[ExternalSourceResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
