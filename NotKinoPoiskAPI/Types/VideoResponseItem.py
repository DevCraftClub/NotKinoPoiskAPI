from dataclasses import dataclass

from NotKinoPoiskAPI.Enums.VideoResponseItemSite import VideoResponseItemSite


@dataclass
class VideoResponseItem:
	url: str
	name: str
	site: VideoResponseItemSite
