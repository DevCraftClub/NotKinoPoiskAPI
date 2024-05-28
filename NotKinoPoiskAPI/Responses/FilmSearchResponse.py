from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.FilmSearchResponseFilm import FilmSearchResponseFilm


@dataclass
class FilmSearchResponse:
	"""
	Объект ответа на поиск фильмов
	"""
	keyword: str
	"""Ключевое слово поиска"""
	pagesCount: int
	"""Количество страниц"""
	searchFilmsCountResult: int
	"""Количество фильмов"""
	films: List[FilmSearchResponseFilm] = field(default_factory=list)
	"""Список найденных фильмов"""

	def __post_init__(self):
		self.films = ObjectController.list_to_object(self.films, FilmSearchResponseFilm)

	def add_films(self, films: Union[FilmSearchResponseFilm, list[FilmSearchResponseFilm]]):
		"""
		Добавление фильмов

		Args:
			films (Union[FilmSearchResponseFilm, list[FilmSearchResponseFilm]]): Фильм или список фильмов
		"""
		if isinstance(films, list):
			self.films.extend(films)
		else:
			self.films.append(films)
