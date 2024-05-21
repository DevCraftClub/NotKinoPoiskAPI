from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@data
class FilmSearchResponseFilm:
	filmId: NonNull[int]
	nameRu: NonNull[str]
	nameEn: NonNull[str]
	type: NonNull[MovieType]
	year: NonNull[int]
	description: NonNull[str]
	filmLength: NonNull[int]
	countries: list[Country] = []
	genres: list[Genre] = []
	rating: NonNull[str]
	ratingVoteCount: NonNull[int]
	posterUrl: Optional[str]
	posterUrlPreview: Optional[str]

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
