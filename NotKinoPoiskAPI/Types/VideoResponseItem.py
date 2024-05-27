from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.VideoResponseItemSite import VideoResponseItemSite


@dataclass
class VideoResponseItem:
	"""
	Класс для хранения информации о видео.
	"""
	url: str
	"""Ссылка на видео"""
	name: str
	"""Название видео"""
	site: VideoResponseItemSite
	"""Сайт, на котором находится видео"""

	def __post_init__(self):
		if isinstance(self.site, str):
			self.site = ObjectController.find_enum(self.site, VideoResponseItemSite)
