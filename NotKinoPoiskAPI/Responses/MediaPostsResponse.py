from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.MediaPostsResponseItem import MediaPostsResponseItem


@dataclass
class MediaPostsResponse(GeneralResponse):
	"""
	Класс для хранения информации о постах.
	"""
	totalPages: int = 0
	"""Количество страниц"""
	items: List[MediaPostsResponseItem] = field(default_factory=list)
	"""Список постов"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, MediaPostsResponseItem)

	def add_item(self, item: Union[MediaPostsResponseItem, list[MediaPostsResponseItem]]):
		"""
		Добавление поста

		Args:
			item (Union[MediaPostsResponseItem, list[MediaPostsResponseItem]]): Пост или список постов
		"""
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)
