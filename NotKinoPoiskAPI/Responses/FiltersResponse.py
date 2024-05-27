from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.FiltersResponseCountry import FiltersResponseCountry
from NotKinoPoiskAPI.Types.FiltersResponseGenre import FiltersResponseGenre


@dataclass
class FiltersResponse:
	"""
	Объект ответа на поиск фильтров
	"""
	genres: List[FiltersResponseGenre] = field(default_factory=list)
	"""Список жанров"""
	countries: List[FiltersResponseCountry] = field(default_factory=list)
	"""Список стран"""

	def __post_init__(self):
		self.genres = ObjectController.list_to_object(self.genres, FiltersResponseGenre)
		self.countries = ObjectController.list_to_object(self.countries, FiltersResponseCountry)

	def add_genre(self, genre: Union[FiltersResponseGenre, list[FiltersResponseGenre]]):
		"""
		Добавление жанра

		:param Union[FiltersResponseGenre, list[FiltersResponseGenre]] genre: Жанр или список жанров
		"""
		if isinstance(genre, list):
			self.genres.extend(genre)
		else:
			self.genres.append(genre)

	def add_country(self, country: Union[FiltersResponseCountry, list[FiltersResponseCountry]]):
		"""
		Добавление страны

		:param Union[FiltersResponseCountry, list[FiltersResponseCountry]] country: Страна или список стран
		"""
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)
