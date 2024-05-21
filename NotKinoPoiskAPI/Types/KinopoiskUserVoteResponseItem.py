from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@data
class KinopoiskUserVoteResponseItem:
	"""
	Класс для хранения информации о голосе пользователя.
	:param kinopoiskId: ID фильма.
	:param nameRu: Русское название фильма.
	:param nameEn: Английское название фильма.
	:param nameOriginal: Оригинальное название фильма.
	:param countries: Список стран производства фильма.
	:param genres: Список жанров фильма.
	:param ratingKinopoisk: Рейтинг фильма на Кинопоиске.
	:param ratingImdb: Рейтинг фильма на IMDB.
	:param year: Год выпуска фильма.
	:param type: Тип медиа.
	:param posterUrl: Ссылка на постер фильма.
	:param posterUrlPreview: Ссылка на превью постера фильма.
	:param userRating: Рейтинг пользователя.
	"""
	kinopoiskId: NonNull[int]
	nameRu: Optional[str]
	nameEn: Optional[str]
	nameOriginal: Optional[str]
	countries: list[Country] = []
	genres: list[Genre] = []
	ratingKinopoisk: Optional[float]
	ratingImdb: Optional[float]
	year: Optional[int]
	type: Optional[MovieType]
	posterUrl: NonNull[str]
	posterUrlPreview: NonNull[str]
	userRating: NonNull[int]

	def add_country(self, country: Union[Country, list[Country]]):
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)

	def add_genres(self, genres: Union[Genre, list[Genre]]):
		if isinstance(genres, list):
			self.genres.extend(genres)
		else:
			self.genres.append(genres)

	def __str__(self):
		title = self.nameRu
		title += f" / {self.nameEn}" if self.nameEn else ""
		title += f" / {self.nameOriginal}" if self.nameOriginal else ""
		title += f" ({self.year})" if self.year else ""
		title += f" [КП: {self.ratingKinopoisk}, IMDb: {self.ratingImdb}, Рейтинг: {self.userRating}]"

		return title.strip()