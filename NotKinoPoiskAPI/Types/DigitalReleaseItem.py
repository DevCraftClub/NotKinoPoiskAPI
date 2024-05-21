from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@data
class DigitalReleaseItem:
	"""
	Класс для хранения информации о цифровом релизе.
	:param filmId: ID фильма.
	:param nameRu: Русское название фильма.
	:param nameEn: Английское название фильма.
	:param year: Год выпуска фильма.
	:param posterUrl: Ссылка на постер фильма.
	:param posterUrlPreview: Ссылка на превью постера фильма.
	:param countries: Список стран производства фильма.
	:param genres: Список жанров фильма.
	:param rating: Рейтинг фильма.
	:param ratingVoteCount: Количество голосов за рейтинг фильма.
	:param expectationsRating: Рейтинг ожиданий фильма.
	:param expectationsRatingVoteCount: Количество голосов за рейтинг ожиданий фильма.
	:param duration: Длительность фильма.
	:param releaseDate: Дата релиза фильма.
	"""
	filmId: NonNull[int]
	nameRu: NonNull[str]
	nameEn: NonNull[str]
	year: NonNull[int]
	posterUrl: NonNull[str]
	posterUrlPreview: NonNull[str]
	countries: list[Country] = []
	genres: list[Genre] = []
	rating: NonNull[float]
	ratingVoteCount: NonNull[int]
	expectationsRating: NonNull[float]
	expectationsRatingVoteCount: NonNull[int]
	duration: NonNull[int]
	releaseDate: NonNull[str]

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
		title += f" ({self.year})" if self.year else ""

		return str(title).strip()
