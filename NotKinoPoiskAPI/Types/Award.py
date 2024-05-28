from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.AwardPerson import AwardPerson


@dataclass
class Award:
	"""
	Класс для хранения информации о награде.
	"""
	name: str
	"""Название награды"""
	win: bool
	"""Победил ли"""
	imageUrl: Optional[str]
	"""Ссылка на изображение"""
	nominationName: str
	"""Название номинации"""
	year: int
	"""Год"""
	persons: List[AwardPerson] = field(default_factory=list)
	"""Список награжденных"""

	def __post_init__(self):
		self.persons = ObjectController.list_to_object(self.persons, AwardPerson)

	def add_person(self, person: Union[AwardPerson, List[AwardPerson]]):
		"""
		Добавление награжденного

		Args:
			person (Union[AwardPerson, List[AwardPerson]]): Награжденный или список награжденных
		"""
		if isinstance(person, list):
			self.persons.extend(person)
		else:
			self.persons.append(person)
