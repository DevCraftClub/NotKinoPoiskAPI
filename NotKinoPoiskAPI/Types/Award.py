from typing import Optional, Union, List

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.AwardPerson import AwardPerson


@dataclass
class Award:
	name: str
	win: bool
	imageUrl: Optional[str]
	nominationName: str
	year: int
	persons: List[AwardPerson] = field(default_factory=list)

	def __post_init__(self):
		self.persons = ObjectController.list_to_object(self.persons, AwardPerson)

	def add_person(self, person: Union[AwardPerson, List[AwardPerson]]):
		if isinstance(person, list):
			self.persons.extend(person)
		else:
			self.persons.append(person)
