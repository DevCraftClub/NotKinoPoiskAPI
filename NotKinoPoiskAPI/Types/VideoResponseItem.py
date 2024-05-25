from dataclasses import dataclass

from NotKinoPoiskAPI.Enums.VideoResponseItemSite import VideoResponseItemSite


@dataclass
class VideoResponseItem:
	url: str
	name: str
	site: VideoResponseItemSite

	def __post_init__(self):
		self.site = VideoResponseItemSite(self.site)
