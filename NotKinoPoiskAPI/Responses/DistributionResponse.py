from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Distribution import Distribution


@data
class DistributionResponse(GeneralResponse):
	"""
	Объект ответа на поиск дистрибьюторов
	:param total: Количество найденных дистрибьюторов
	:param items: Список найденных дистрибьюторов
	"""
	items: list[Distribution] = []

	def add_distribution(self, distribution: Union[Distribution, list[Distribution]]):
		if isinstance(distribution, list):
			self.items.extend(distribution)
		else:
			self.items.append(distribution)
