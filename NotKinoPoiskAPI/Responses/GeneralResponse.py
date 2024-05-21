from paprika import NonNull, data


@data
class GeneralResponse:
	"""
	Объект ответа
	:param total: Количество найденных объектов
	:param items: Список найденных объектов
	"""
	total: NonNull[int]
	items: list = []
