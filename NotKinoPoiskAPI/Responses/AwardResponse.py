from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Award import Award


@data
class AwardResponse(GeneralResponse):
	"""
	Объект ответа на поиск наград
	:param total: Количество найденных наград
	:param items: Список найденных наград
	"""
	items: list[Award] = []

	def add_award(self, award: Union[Award, list[Award]]):
		if isinstance(award, Award):
			self.items.append(award)
		else:
			self.items.extend(award)
