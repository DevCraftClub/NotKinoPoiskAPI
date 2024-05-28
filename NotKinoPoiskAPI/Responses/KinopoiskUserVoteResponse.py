from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.KinopoiskUserVoteResponseItem import KinopoiskUserVoteResponseItem


@dataclass
class KinopoiskUserVoteResponse(GeneralResponse):
	"""
	Класс для хранения информации о голосах пользователя.
	"""
	totalPages: int = 0
	"""Количество страниц"""
	items: List[KinopoiskUserVoteResponseItem] = field(default_factory=list)
	"""Список голосов"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, KinopoiskUserVoteResponseItem)

	def add_item(self, item: Union[KinopoiskUserVoteResponseItem, list[KinopoiskUserVoteResponseItem]]):
		"""
		Добавление голоса

		Args:
			item (Union[KinopoiskUserVoteResponseItem, list[KinopoiskUserVoteResponseItem]]): Голос или список голосов
		"""
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)
