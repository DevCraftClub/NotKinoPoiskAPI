from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.FiltersResponseCountry import FiltersResponseCountry
from NotKinoPoiskAPI.Types.FiltersResponseGenre import FiltersResponseGenre


@dataclass
class FiltersResponse:
	"""
	Объект ответа на поиск фильтров
	:param genres: Список жанров
	:param countries: Список стран
	"""
	genres: List[FiltersResponseGenre] = field(default_factory=list)
	countries: List[FiltersResponseCountry] = field(default_factory=list)

	def __post_init__(self):
		self.genres = ObjectController.list_to_object(self.genres, FiltersResponseGenre)
		self.countries = ObjectController.list_to_object(self.countries, FiltersResponseCountry)

	def add_genre(self, genre: Union[FiltersResponseGenre, list[FiltersResponseGenre]]):
		if isinstance(genre, list):
			self.genres.extend(genre)
		else:
			self.genres.append(genre)

	def add_country(self, country: Union[FiltersResponseCountry, list[FiltersResponseCountry]]):
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)
