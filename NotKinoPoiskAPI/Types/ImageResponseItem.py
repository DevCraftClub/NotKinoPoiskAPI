from paprika import NonNull, data


@data
class ImageResponseItem:
	imageUrl: NonNull[str]
	previewUrl: NonNull[str]
