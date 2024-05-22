from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.VideoResponseItem import VideoResponseItem


@dataclass
class VideoResponse(GeneralResponse):
	"""
	Класс для хранения информации о видео.
	:param total: Количество видео.
	:param items: Список видео.
	"""
	items: list[VideoResponseItem] = field(default_factory=list)

	def add_item(self, item: Union[VideoResponseItem, list[VideoResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)

