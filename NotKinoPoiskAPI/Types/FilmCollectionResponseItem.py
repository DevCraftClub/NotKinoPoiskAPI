from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class FilmCollectionResponseItem:
	"""
	Объект фильма или сериала
	"""
	kinopoiskId: int
	"""Идентификатор фильма"""
	nameRu: Optional[str]
	"""Название фильма"""
	nameEn: Optional[str]
	"""Название фильма на английском"""
	nameOriginal: Optional[str]
	"""Оригинальное название фильма"""
	ratingKinopoisk: Optional[float]
	"""Рейтинг КиноПоиск"""
	ratingImdb: Optional[float]
	"""Рейтинг IMDB"""
	year: Optional[int]
	"""Год выпуска фильма"""
	type: Optional[MovieType]
	"""Тип фильма"""
	posterUrl: str
	"""Ссылка на постер"""
	posterUrlPreview: str
	"""Ссылка на превью постера"""
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

		:param Union[Country, list[Country]] country: Страна или список стран
		"""
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)

	def add_genres(self, genres: Union[Genre, list[Genre]]):
		"""
		Добавление жанра

		:param Union[Genre, list[Genre]] genres: Жанр или список жанров
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
