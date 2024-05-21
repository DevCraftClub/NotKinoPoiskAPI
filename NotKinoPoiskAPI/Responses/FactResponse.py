from typing import Union

from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Fact import Fact


@data
class FactResponse(GeneralResponse):
	"""
	Объект ответа на поиск фактов
	:param total: Количество найденных фактов
	:param items: Список найденных фактов
	"""
	items: list[Fact] = []

	def add_fact(self, fact: Union[Fact, list[Fact]]):
		if isinstance(fact, Fact):
			self.items.append(fact)
		else:
			self.items.extend(fact)
