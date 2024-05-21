from typing import Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Types.FilmSearchResponseFilm import FilmSearchResponseFilm


@dataclass
class FilmSearchResponse:
	keyword: str
	pagesCount: int
	searchFilmsCountResult: int
	films: list[FilmSearchResponseFilm] = field(default_factory=list)

	def add_films(self, films: Union[FilmSearchResponseFilm, list[FilmSearchResponseFilm]]):
		if isinstance(films, list):
			self.films.extend(films)
		else:
			self.films.append(films)
