from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Types.FiltersResponseCountry import FiltersResponseCountry
from NotKinoPoiskAPI.Types.FiltersResponseGenre import FiltersResponseGenre


@dataclass
class FiltersResponse:
	"""
	Объект ответа на поиск фильтров
	:param genres: Список жанров
	:param countries: Список стран
	"""
	genres: list[FiltersResponseGenre] = field(default_factory=list)
	countries: list[FiltersResponseCountry] = field(default_factory=list)

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
