from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.VideoResponseItemSite import VideoResponseItemSite


@dataclass
class VideoResponseItem:
	url: str
	name: str
	site: VideoResponseItemSite

	def __post_init__(self):
		if isinstance(self.site, str):
			self.site = ObjectController.find_enum(self.site, VideoResponseItemSite)
