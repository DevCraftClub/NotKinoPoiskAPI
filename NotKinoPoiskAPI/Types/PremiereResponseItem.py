from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class PremiereResponseItem:
	"""
	Объект премьеры фильма или сериала
	"""
	kinopoiskId: int
	"""Идентификатор фильма"""
	nameRu: Optional[str]
	"""Название фильма"""
	nameEn: Optional[str]
	"""Название фильма на английском"""
	year: int
	"""Год премьеры фильма"""
	posterUrl: str
	"""Ссылка на постер"""
	posterUrlPreview: str
	"""Ссылка на превью постера"""
	duration: Optional[int]
	"""Длительность фильма"""
	premiereRu: str
	"""Дата премьеры в РФ"""
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
		title += f" [Премьера: {self.premiereRu}]"

		return str(title).strip()
