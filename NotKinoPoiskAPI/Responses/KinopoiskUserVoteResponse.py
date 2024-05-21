from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.KinopoiskUserVoteResponseItem import KinopoiskUserVoteResponseItem


@data
class KinopoiskUserVoteResponse(GeneralResponse):
	"""
	Класс для хранения информации о голосах пользователя.
	:param total: Количество голосов.
	:param totalPages: Количество страниц.
	:param items: Список голосов.
	"""
	totalPages: NonNull[int]
	items: list[KinopoiskUserVoteResponseItem] = []

	def add_item(self, item: Union[KinopoiskUserVoteResponseItem, list[KinopoiskUserVoteResponseItem]]):
		if isinstance(item, list):
			self.items.extend(item)
		else:
			self.items.append(item)
