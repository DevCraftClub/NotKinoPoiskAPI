from enum import Enum


class CollectionType(Enum):
	"""Типы коллекций"""
	TOP_POPULAR_ALL = "Популярные"
	"""Популярные"""
	TOP_POPULAR_MOVIES = "Популярные фильмы"
	"""Популярные фильмы"""
	TOP_250_TV_SHOWS = "ТОП 250 сериалов"
	"""ТОП 250 сериалов"""
	TOP_250_MOVIES = "Топ 250 фильмов"
	"""Топ 250 фильмов"""
	VAMPIRE_THEME = "Про вампиров"
	"""Про вампиров"""
	COMICS_THEME = "По мотивам комиксов"
	"""По мотивам комиксов"""
	CLOSES_RELEASES = "Закрытые показы"
	"""Закрытые показы"""
	FAMILY = "Семейные"
	"""Семейные"""
	OSKAR_WINNERS_2021 = "Оскар 2021"
	"""Оскар 2021"""
	LOVE_THEME = "Любовные"
	"""Любовные"""
	ZOMBIE_THEME = "Про зомби"
	"""Про зомби"""
	CATASTROPHE_THEME = "Про катастрофы"
	"""Про катастрофы"""
	KIDS_ANIMATION_THEME = "Мультфильмы"
	"""Мультфильмы"""
	POPULAR_SERIES = "Популярные сериалы"
	"""Популярные сериалы"""
