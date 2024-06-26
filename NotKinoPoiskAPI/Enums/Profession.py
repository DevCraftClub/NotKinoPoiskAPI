from enum import Enum


class Profession(Enum):
	"""Типы профессий"""
	DIRECTOR = "Режиссёр"
	"""Режиссёр"""
	ACTOR = "Актёр"
	"""Актёр"""
	PRODUCER = "Продюсер"
	"""Продюсер"""
	WRITER = "Сценарист"
	"""Сценарист"""
	OPERATOR = "Оператор"
	"""Оператор"""
	EDITOR = "Монтажёр"
	"""Монтажёр"""
	COMPOSER = "Композитор"
	"""Композитор"""
	PRODUCER_USSR = "Продюсер СССР"
	"""Продюсер СССР"""
	TRANSLATOR = "Переводчик"
	"""Переводчик"""
	DESIGN = "Художник"
	"""Художник"""
	VOICE_DIRECTOR = "Режиссёр дубляжа"
	"""Режиссёр дубляжа"""
	UNKNOWN = "Неизвестно"
	"""Неизвестно"""
	HIMSELF = "Сам себя"
	"""Сам себя"""
	HERSELF = "Сама себя"
	"""Сама себя"""
	HRONO_TITR_MALE = "Хронотитраж мужской"
	"""Хронотитраж мужской"""
	HRONO_TITR_FEMALE = "Хронотитраж женский"
	"""Хронотитраж женский"""
