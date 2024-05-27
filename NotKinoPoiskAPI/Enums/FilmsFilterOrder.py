from enum import Enum


class FilmFilterOrder(Enum):
	"""Тип порядка фильтрации фильмов"""
	RATING = 'По рейтингу'
	"""По рейтингу"""
	NUM_VOTE = 'По количеству голосов'
	"""По количеству голосов"""
	YEAR = 'По годам'
	"""По годам"""
