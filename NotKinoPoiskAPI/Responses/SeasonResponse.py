from dataclasses import dataclass, field
from typing import Union, List

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Season import Season


@dataclass
class SeasonResponse(GeneralResponse):
	"""
	Объект ответа на поиск сезонов
	:param total: Количество найденных сезонов
	:param items: Список найденных сезонов
	"""
	items: List[Season] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, Season)

	def add_season(self, season: Union[Season, List[Season]]):
		if isinstance(season, list):
			self.items.extend(season)
		else:
			self.items.append(season)
