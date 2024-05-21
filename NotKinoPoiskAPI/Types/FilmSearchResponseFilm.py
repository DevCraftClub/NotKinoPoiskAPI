from typing import Optional, Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class FilmSearchResponseFilm:
	filmId: int
	nameRu: str
	nameEn: str
	type: MovieType
	year: int
	description: str
	filmLength: int
	rating: str
	ratingVoteCount: int
	posterUrl: Optional[str]
	posterUrlPreview: Optional[str]
	countries: list[Country] = field(default_factory=list)
	genres: list[Genre] = field(default_factory=list)

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
