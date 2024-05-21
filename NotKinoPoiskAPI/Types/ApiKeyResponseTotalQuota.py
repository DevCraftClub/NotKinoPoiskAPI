from dataclasses import dataclass


@dataclass
class ApiKeyResponseTotalQuota:
	"""
	Класс для хранения информации о ключе API.
	:param value: Общее количество запросов.
	:param used: Количество использованных запросов.
	"""
	value: int
	used: int
	