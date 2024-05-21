from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmCollectionResponseItem import FilmCollectionResponseItem


@data
class FilmCollectionResponse(GeneralResponse):
	"""
	Класс для хранения информации о коллекции фильмов.
	:param total: Количество фильмов.
	:param totalPages: Количество страниц.
	:param items: Список фильмов.
	"""
	totalPages: NonNull[int]
	items: list[FilmCollectionResponseItem] = []

	def add_items(self, items: Union[FilmCollectionResponseItem, list[FilmCollectionResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
