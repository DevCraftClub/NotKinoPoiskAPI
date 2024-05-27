from dataclasses import dataclass


@dataclass
class MediaPostsResponseItem:
	"""
	Класс для хранения информации о медиа-посте.
	"""
	kinopoiskId: int
	"""ID фильма на КиноПоиске"""
	imageUrl: str
	"""Ссылка на изображение"""
	title: str
	"""Название фильма"""
	description: str
	"""Описание фильма"""
	url: str
	"""Ссылка на фильм"""
	publishedAt: str
	"""Дата публикации"""
