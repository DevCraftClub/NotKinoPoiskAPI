from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.Award import Award


@dataclass
class AwardResponse(GeneralResponse):
	"""
	Объект ответа на поиск наград
	"""
	items: list[Award] = field(default_factory=list)
	"""Список найденных наград"""

	def __post_init__(self):
		if self.items is None:
			self.items = list()
		else:
			self.items = [Award(**award) if isinstance(award, dict) else award for award in self.items]

	def add_award(self, award: Union[Award, list[Award]]):
		"""
		Добавление награды

		Args:
			award (Union[Award, list[Award]]): Награда или список наград
		"""
		if isinstance(award, Award):
			self.items.append(award)
		else:
			self.items.extend(award)
