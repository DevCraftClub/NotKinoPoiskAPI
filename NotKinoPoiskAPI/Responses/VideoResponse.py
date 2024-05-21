from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.VideoResponseItem import VideoResponseItem


@data
class VideoResponse(GeneralResponse):
	"""
	Класс для хранения информации о видео.
	:param total: Количество видео.
	:param items: Список видео.
	"""
	items: list[VideoResponseItem] = []

	def add_item(self, item: Union[VideoResponseItem, list[VideoResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)

