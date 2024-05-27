from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmCollectionResponseItem import FilmCollectionResponseItem


@dataclass
class FilmCollectionResponse(GeneralResponse):
	"""
	Класс для хранения информации о коллекции фильмов.
	"""
	items: List[FilmCollectionResponseItem] = field(default_factory=list)
	"""Список найденных фильмов"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, FilmCollectionResponseItem)

	def add_items(self, items: Union[FilmCollectionResponseItem, list[FilmCollectionResponseItem]]):
		"""
		Добавление фильмов

		:param Union[FilmCollectionResponseItem, list[FilmCollectionResponseItem]] items: Фильм или список фильмов
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
