from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.BoxOffice import BoxOffice


@data
class BoxOfficeResponse(GeneralResponse):
	"""
	Объект ответа на поиск кассовых сборов
	:param total: Количество найденных кассовых сборов
	:param items: Список найденных кассовых сборов
	"""
	items: list[BoxOffice] = []

	def add_box_office(self, box_office: Union[BoxOffice, list[BoxOffice]]):
		if isinstance(box_office, list):
			self.items.extend(box_office)
		else:
			self.items.append(box_office)
			