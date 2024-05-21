from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ExternalSourceResponseItem import ExternalSourceResponseItem


@data
class ExternalSourceResponse(GeneralResponse):
	"""
	Класс для хранения информации о внешних источниках.
	"""
	items: list[ExternalSourceResponseItem] = []

	def add_items(self, items: Union[ExternalSourceResponseItem, list[ExternalSourceResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
