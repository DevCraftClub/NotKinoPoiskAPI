from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.FilmSearchResponseFilm import FilmSearchResponseFilm


@data
class FilmSearchResponse:
	keyword: NonNull[str]
	pagesCount: NonNull[int]
	searchFilmsCountResult: NonNull[int]
	films: list[FilmSearchResponseFilm] = []

	def add_films(self, films: Union[FilmSearchResponseFilm, list[FilmSearchResponseFilm]]):
		if isinstance(films, list):
			self.films.extend(films)
		else:
			self.films.append(films)
