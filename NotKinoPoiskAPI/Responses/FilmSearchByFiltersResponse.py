from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.FilmSearchByFiltersResponseItem import FilmSearchByFiltersResponseItem


@dataclass
class FilmSearchByFiltersResponse(GeneralResponse):
	"""
	Объект ответа на поиск фильмов по фильтрам
	:param total: Количество найденных фильмов
	:param totalPages: Количество страниц
	:param items: Список найденных фильмов
	"""
	items: list[FilmSearchByFiltersResponseItem] = field(default_factory=list)

	def add_items(self, items: Union[FilmSearchByFiltersResponseItem, list[FilmSearchByFiltersResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
