from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmResponseFilm import FilmResponseFilm


@dataclass
class RelatedFilmResponse(GeneralResponse):
	"""
	Класс для хранения информации о связанных фильмах.
	"""
	items: List[FilmResponseFilm] = field(default_factory=list)
	"""Список фильмов"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, FilmResponseFilm)

	def add_items(self, items: Union[FilmResponseFilm, List[FilmResponseFilm]]):
		"""
		Добавление фильмов

		Args:
			items (Union[FilmResponseFilm, List[FilmResponseFilm]]): Фильм или список фильмов
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
