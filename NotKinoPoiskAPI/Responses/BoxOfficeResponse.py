from dataclasses import dataclass, field
from typing import Union, List

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.BoxOffice import BoxOffice


@dataclass
class BoxOfficeResponse(GeneralResponse):
	"""
	Объект ответа на поиск кассовых сборов
	:param total: Количество найденных кассовых сборов
	:param items: Список найденных кассовых сборов
	"""
	items: List[BoxOffice] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, BoxOffice)

	def add_box_office(self, box_office: Union[BoxOffice, list[BoxOffice]]):
		if isinstance(box_office, list):
			self.items.extend(box_office)
		else:
			self.items.append(box_office)
