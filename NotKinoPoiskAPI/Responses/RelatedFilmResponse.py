from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmResponseFilm import FilmResponseFilm


@dataclass
class RelatedFilmResponse(GeneralResponse):
	"""
	Класс для хранения информации о связанных фильмах.
	"""
	items: list[FilmResponseFilm] = field(default_factory=list)

	def add_items(self, items: Union[FilmResponseFilm, list[FilmResponseFilm]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
			