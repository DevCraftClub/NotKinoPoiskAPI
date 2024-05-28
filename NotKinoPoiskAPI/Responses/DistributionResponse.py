from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Distribution import Distribution


@dataclass
class DistributionResponse(GeneralResponse):
	"""
	Объект ответа на поиск дистрибьюторов
	"""
	items: List[Distribution] = field(default_factory=list)
	"""Список найденных дистрибьюторов"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, Distribution)

	def add_distribution(self, distribution: Union[Distribution, list[Distribution]]):
		"""
		Добавление дистрибьютора

		Args:
			distribution (Union[Distribution, list[Distribution]]): Дистрибьютор или список дистрибьюторов
		"""
		if isinstance(distribution, list):
			self.items.extend(distribution)
		else:
			self.items.append(distribution)
