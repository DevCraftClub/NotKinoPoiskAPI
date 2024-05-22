from enum import Enum


class DistributionType(Enum):
	LOCAL = "Местный"
	COUNTRY_SPECIFIC = "Специфичный для страны"
	PREMIERE = "Премьера"
	ALL = "Все"
	WORLD_PREMIER = "Всемирная премьера"
