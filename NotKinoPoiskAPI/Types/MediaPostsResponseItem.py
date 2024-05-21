from paprika import NonNull, data


@data
class MediaPostsResponseItem:
	kinopoiskId: NonNull[int]
	imageUrl: NonNull[str]
	title: NonNull[str]
	description: NonNull[str]
	url: NonNull[str]
	publishedAt: NonNull[str]
