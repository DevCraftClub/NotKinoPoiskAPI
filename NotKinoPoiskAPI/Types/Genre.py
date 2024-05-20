from paprika import data, NonNull


@data
class Genre:
	"""
	Объект жанра
	:param genre: Название жанра
	"""
	genre: NonNull[str]
