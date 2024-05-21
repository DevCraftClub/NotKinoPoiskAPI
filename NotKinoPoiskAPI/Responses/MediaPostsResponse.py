from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.MediaPostsResponseItem import MediaPostsResponseItem


@data
class MediaPostsResponse(GeneralResponse):
	"""
	Класс для хранения информации о постах.
	:param total: Количество постов.
	:param totalPages: Количество страниц.
	:param items: Список постов.
	"""
	totalPages: NonNull[int]
	items: list[MediaPostsResponseItem] = []

	def add_item(self, item: Union[MediaPostsResponseItem, list[MediaPostsResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)

