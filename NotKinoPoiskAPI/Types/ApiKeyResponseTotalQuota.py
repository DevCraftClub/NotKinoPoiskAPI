from paprika import NonNull, data


@data
class ApiKeyResponseTotalQuota:
	"""
	Класс для хранения информации о ключе API.
	:param value: Общее количество запросов.
	:param used: Количество использованных запросов.
	"""
	value: NonNull[int]
	used: NonNull[int]
	