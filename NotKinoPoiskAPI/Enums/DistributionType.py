from enum import Enum


class DistributionType(Enum):
	"""Типы дистрибуции"""
	LOCAL = "Местный"
	"""Местный"""
	COUNTRY_SPECIFIC = "Специфичный для страны"
	"""Специфичный для страны"""
	PREMIERE = "Премьера"
	"""Премьера"""
	ALL = "Все"
	"""Все"""
	WORLD_PREMIER = "Всемирная премьера"
	"""Всемирная премьера"""
