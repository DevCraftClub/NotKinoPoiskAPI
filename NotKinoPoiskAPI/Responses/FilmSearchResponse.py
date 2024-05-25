from typing import Union, List

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.FilmSearchResponseFilm import FilmSearchResponseFilm


@dataclass
class FilmSearchResponse:
	keyword: str
	pagesCount: int
	searchFilmsCountResult: int
	films: List[FilmSearchResponseFilm] = field(default_factory=list)

	def __post_init__(self):
		self.films = ObjectController.list_to_object(self.films, FilmSearchResponseFilm)

	def add_films(self, films: Union[FilmSearchResponseFilm, list[FilmSearchResponseFilm]]):
		if isinstance(films, list):
			self.films.extend(films)
		else:
			self.films.append(films)
