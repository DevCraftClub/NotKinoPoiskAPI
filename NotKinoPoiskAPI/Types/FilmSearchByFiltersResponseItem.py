from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@data
class FilmSearchByFiltersResponseItem:
	kinopoiskId: NonNull[int]
	imdbId: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	nameOriginal: Optional[str]
	countries: list[Country] = []
	genres: list[Genre] = []
	ratingKinopoisk: Optional[float]
	ratingImdb: Optional[float]
	year: Optional[int]
	type: Optional[MovieType]
	posterUrl: NonNull[str]
	posterUrlPreview: NonNull[str]

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

		return title.strip()
