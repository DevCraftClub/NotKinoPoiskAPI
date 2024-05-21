from typing import Optional, Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Types.AwardPerson import AwardPerson


@dataclass
class Award:
	name: str
	win: bool
	imageUrl: Optional[str]
	nominationName: str
	year: int
	persons: list[AwardPerson] = field(default_factory=list)

	def add_person(self, person: Union[AwardPerson, list[AwardPerson]]):
		if isinstance(person, list):
			self.persons.extend(person)
		else:
			self.persons.append(person)
