from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
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
	kinopoiskId: int
	nameRu: Optional[str]
	nameEn: Optional[str]
	nameOriginal: Optional[str]
	ratingKinopoisk: Optional[float]
	ratingImdb: Optional[float]
	year: Optional[int]
	type: Optional[MovieType]
	posterUrl: str
	posterUrlPreview: str
	userRating: int
	countries: List[Country] = field(default_factory=list)
	genres: List[Genre] = field(default_factory=list)

	def __post_init__(self):
		self.countries = ObjectController.list_to_object(self.countries, Country)
		self.genres = ObjectController.list_to_object(self.genres, Genre)
		if self.type is not None and isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, MovieType)

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
