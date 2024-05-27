from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.ImageResponseItem import ImageResponseItem


@dataclass
class ImageResponse(GeneralResponse):
	"""
	Класс для хранения информации об изображениях.
	"""
	items: List[ImageResponseItem] = field(default_factory=list)
	"""Список найденных изображений"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, ImageResponseItem)

	def add_items(self, items: Union[ImageResponseItem, list[ImageResponseItem]]):
		"""
		Добавление изображений

		:param Union[ImageResponseItem, list[ImageResponseItem]] items: Изображение или список изображений
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
