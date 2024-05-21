from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Season import Season


@data
class SeasonResponse(GeneralResponse):
	"""
	Объект ответа на поиск сезонов
	:param total: Количество найденных сезонов
	:param items: Список найденных сезонов
	"""
	items: list[Season] = []

	def add_season(self, season: Union[Season, list[Season]]):
		if isinstance(season, list):
			self.items.extend(season)
		else:
			self.items.append(season)
