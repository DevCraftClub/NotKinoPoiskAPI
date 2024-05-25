from dataclasses import dataclass, field
from typing import Union, List

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Fact import Fact


@dataclass
class FactResponse(GeneralResponse):
	"""
	Объект ответа на поиск фактов
	:param total: Количество найденных фактов
	:param items: Список найденных фактов
	"""
	items: List[Fact] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, Fact)

	def add_fact(self, fact: Union[Fact, list[Fact]]):
		if isinstance(fact, Fact):
			self.items.append(fact)
		else:
			self.items.extend(fact)
