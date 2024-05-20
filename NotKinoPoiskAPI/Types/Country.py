from paprika import NonNull, data


@data
class Country:
	"""
	Объект страны
	:param country: Название страны
	"""
	country: NonNull[str]
