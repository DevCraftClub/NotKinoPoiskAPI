from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ImageResponseItem import ImageResponseItem


@dataclass
class ImageResponse(GeneralResponse):
	"""
	Класс для хранения информации об изображениях.
	"""
	items: list[ImageResponseItem] = field(default_factory=list)

	def add_items(self, items: Union[ImageResponseItem, list[ImageResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
