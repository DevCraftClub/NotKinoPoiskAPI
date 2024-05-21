from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.PersonByNameResponseItem import PersonByNameResponseItem


@data
class PersonByNameResponse(GeneralResponse):
	"""
	Класс для хранения информации о персоне по имени.
	:param total: Количество персон.
	:param items: Список персон.
	"""
	items: list[PersonByNameResponseItem] = []

	def add_items(self, items: Union[PersonByNameResponseItem, list[PersonByNameResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
