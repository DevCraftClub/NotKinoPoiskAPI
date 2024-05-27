from dataclasses import dataclass


@dataclass
class ApiKeyResponseTotalQuota:
	"""
	Класс для хранения информации о ключе API.
	"""
	value: int
	"""Общее количество запросов."""
	used: int
	"""Количество использованных запросов."""
