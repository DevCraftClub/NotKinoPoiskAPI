from enum import Enum


class CollectionType(Enum):
	TOP_POPULAR_ALL = "Популярные"
	TOP_POPULAR_MOVIES = "Популярные фильмы"
	TOP_250_TV_SHOWS = "ТОП 250 сериалов"
	TOP_250_MOVIES = "Топ 250 фильмов"
	VAMPIRE_THEME = "Про вампиров"
	COMICS_THEME = "По мотивам комиксов"
	CLOSES_RELEASES = "Закрытые показы"
	FAMILY = "Семейные"
	OSKAR_WINNERS_2021 = "Оскар 2021"
	LOVE_THEME = "Любовные"
	ZOMBIE_THEME = "Про зомби"
	CATASTROPHE_THEME = "Про катастрофы"
	KIDS_ANIMATION_THEME = "Мультфильмы"
	POPULAR_SERIES = "Популярные сериалы"
