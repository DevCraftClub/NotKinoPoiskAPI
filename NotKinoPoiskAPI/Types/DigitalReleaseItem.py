from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class DigitalReleaseItem:
	"""
	Класс для хранения информации о цифровом релизе.
	"""
	filmId: int
	"""ID фильма"""
	nameRu: str
	"""Русское название фильма"""
	nameEn: str
	"""Английское название фильма"""
	year: int
	"""Год выпуска фильма"""
	posterUrl: str
	"""Ссылка на постер фильма"""
	posterUrlPreview: str
	"""Ссылка на превью постера фильма"""
	rating: float
	"""Рейтинг фильма"""
	ratingVoteCount: int
	"""Количество голосов за рейтинг фильма"""
	expectationsRating: float
	"""Рейтинг ожиданий фильма"""
	expectationsRatingVoteCount: int
	"""Количество голосов за рейтинг ожиданий фильма"""
	duration: int
	"""Длительность фильма"""
	releaseDate: str
	"""Дата релиза фильма"""
	countries: List[Country] = field(default_factory=list)
	"""Список стран производства фильма"""
	genres: List[Genre] = field(default_factory=list)
	"""Список жанров фильма"""

	def __post_init__(self):
		self.countries = ObjectController.list_to_object(self.countries, Country)
		self.genres = ObjectController.list_to_object(self.genres, Genre)

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
		title += f" ({self.year})" if self.year else ""

		return str(title).strip()
