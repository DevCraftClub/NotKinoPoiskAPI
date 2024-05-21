from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
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
	filmId: int
	nameRu: str
	nameEn: str
	year: int
	posterUrl: str
	posterUrlPreview: str
	rating: float
	ratingVoteCount: int
	expectationsRating: float
	expectationsRatingVoteCount: int
	duration: int
	releaseDate: str
	countries: list[Country] = field(default_factory=list)
	genres: list[Genre] = field(default_factory=list)

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
