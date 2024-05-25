from typing import Optional, Union, List

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class FilmCollectionResponseItem:
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
	countries: List[Country] = field(default_factory=list)
	genres: List[Genre] = field(default_factory=list)

	def __post_init__(self):
		self.countries = ObjectController.list_to_object(self.countries, Country)
		self.genres = ObjectController.list_to_object(self.genres, Genre)

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