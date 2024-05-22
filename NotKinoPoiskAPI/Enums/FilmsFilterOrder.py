from enum import Enum


class FilmFilterOrder(Enum):
	RATING = 'По рейтингу'
	NUM_VOTE = 'По количеству голосов'
	YEAR = 'По годам'
