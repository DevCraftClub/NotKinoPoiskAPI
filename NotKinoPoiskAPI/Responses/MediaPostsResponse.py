from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.MediaPostsResponseItem import MediaPostsResponseItem


@dataclass
class MediaPostsResponse(GeneralResponse):
	"""
	Класс для хранения информации о постах.
	:param total: Количество постов.
	:param totalPages: Количество страниц.
	:param items: Список постов.
	"""
	totalPages: int
	items: list[MediaPostsResponseItem] = field(default_factory=list)

	def add_item(self, item: Union[MediaPostsResponseItem, list[MediaPostsResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)

