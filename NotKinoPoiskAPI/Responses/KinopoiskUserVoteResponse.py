from dataclasses import dataclass, field
from typing import Union, List

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.KinopoiskUserVoteResponseItem import KinopoiskUserVoteResponseItem


@dataclass
class KinopoiskUserVoteResponse(GeneralResponse):
	"""
	Класс для хранения информации о голосах пользователя.
	:param total: Количество голосов.
	:param totalPages: Количество страниц.
	:param items: Список голосов.
	"""
	totalPages: int
	items: List[KinopoiskUserVoteResponseItem] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, KinopoiskUserVoteResponseItem)

	def add_item(self, item: Union[KinopoiskUserVoteResponseItem, list[KinopoiskUserVoteResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)
