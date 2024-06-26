from dataclasses import dataclass, field
from typing import List

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.PremiereResponseItem import PremiereResponseItem


@dataclass
class PremiereResponse(GeneralResponse):
	"""
	Класс для хранения информации о премьере.
	"""
	items: List[PremiereResponseItem] = field(default_factory=list)
	"""Список премьер"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, PremiereResponseItem)
