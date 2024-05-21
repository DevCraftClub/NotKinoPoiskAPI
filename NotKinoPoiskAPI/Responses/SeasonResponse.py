from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Season import Season


@dataclass
class SeasonResponse(GeneralResponse):
	"""
	Объект ответа на поиск сезонов
	:param total: Количество найденных сезонов
	:param items: Список найденных сезонов
	"""
	items: list[Season] = field(default_factory=list)

	def add_season(self, season: Union[Season, list[Season]]):
		if isinstance(season, list):
			self.items.extend(season)
		else:
			self.items.append(season)
