from dataclasses import dataclass


@dataclass
class MediaPostsResponseItem:
	kinopoiskId: int
	imageUrl: str
	title: str
	description: str
	url: str
	publishedAt: str
