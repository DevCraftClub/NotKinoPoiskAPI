from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ImageResponseItem import ImageResponseItem


@data
class ImageResponse(GeneralResponse):
	"""
	Класс для хранения информации об изображениях.
	"""
	totalPages: NonNull[int]
	items: list[ImageResponseItem] = []

	def add_items(self, items: Union[ImageResponseItem, list[ImageResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
