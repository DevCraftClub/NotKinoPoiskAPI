from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmSearchByFiltersResponseItem import FilmSearchByFiltersResponseItem


@data
class FilmSearchByFiltersResponse(GeneralResponse):
	"""
	Объект ответа на поиск фильмов по фильтрам
	:param total: Количество найденных фильмов
	:param totalPages: Количество страниц
	:param items: Список найденных фильмов
	"""
	totalPages: NonNull[int]
	items: list[FilmSearchByFiltersResponseItem] = []

	def add_items(self, items: Union[FilmSearchByFiltersResponseItem, list[FilmSearchByFiltersResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
