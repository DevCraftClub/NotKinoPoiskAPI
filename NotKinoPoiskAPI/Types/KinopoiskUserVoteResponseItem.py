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
	"""
	kinopoiskId: int
	"""ID фильма"""
	nameRu: Optional[str]
	"""Русское название фильма"""
	nameEn: Optional[str]
	"""Английское название фильма"""
	nameOriginal: Optional[str]
	"""Оригинальное название фильма"""
	ratingKinopoisk: Optional[float]
	"""Рейтинг фильма на Кинопоиске"""
	ratingImdb: Optional[float]
	"""Рейтинг фильма на IMDB"""
	year: Optional[int]
	"""Год выпуска фильма"""
	type: Optional[MovieType]
	"""Тип медиа"""
	posterUrl: str
	"""Ссылка на постер фильма"""
	posterUrlPreview: str
	"""Ссылка на превью постера фильма"""
	userRating: int
	"""Рейтинг пользователя"""
	countries: List[Country] = field(default_factory=list)
	"""Список стран производства фильма"""
	genres: List[Genre] = field(default_factory=list)
	"""Список жанров фильма"""

	def __post_init__(self):
		self.countries = ObjectController.list_to_object(self.countries, Country)
		self.genres = ObjectController.list_to_object(self.genres, Genre)
		if self.type is not None and isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, MovieType)

	def add_country(self, country: Union[Country, list[Country]]):
		"""
		Добавление страны производства

		Args:
			country (Union[Country, list[Country]]): Страна или список стран
		"""
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)

	def add_genres(self, genres: Union[Genre, list[Genre]]):
		"""
		Добавление жанра

		Args:
			genres (Union[Genre, list[Genre]]): Жанр или список жанров
		"""
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
