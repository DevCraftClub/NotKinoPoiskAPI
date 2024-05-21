from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.VideoResponseItemSite import VideoResponseItemSite


@data
class VideoResponseItem:
	url: NonNull[str]
	name: NonNull[str]
	site: NonNull[VideoResponseItemSite]
