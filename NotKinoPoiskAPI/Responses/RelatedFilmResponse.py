from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmResponseFilm import FilmResponseFilm


@data
class RelatedFilmResponse(GeneralResponse):
	"""
	Класс для хранения информации о связанных фильмах.
	"""
	items: list[FilmResponseFilm] = []

	def add_items(self, items: Union[FilmResponseFilm, list[FilmResponseFilm]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
			