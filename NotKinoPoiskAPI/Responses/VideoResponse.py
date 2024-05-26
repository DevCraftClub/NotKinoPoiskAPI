from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.VideoResponseItem import VideoResponseItem


@dataclass
class VideoResponse(GeneralResponse):
	"""
	Класс для хранения информации о видео.
	:param total: Количество видео.
	:param items: Список видео.
	"""
	items: List[VideoResponseItem] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, VideoResponseItem)

	def add_item(self, item: Union[VideoResponseItem, list[VideoResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)
