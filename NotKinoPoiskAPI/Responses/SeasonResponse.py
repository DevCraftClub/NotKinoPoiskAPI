from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.Season import Season


@data
class SeasonResponse:
	total: NonNull[int]
	items: list[Season] = []

	def add_season(self, season: Union[Season, list[Season]]):
		if isinstance(season, list):
			self.items.extend(season)
		else:
			self.items.append(season)