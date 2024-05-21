from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.AwardPerson import AwardPerson


@data
class Award:
	name: NonNull[str]
	win: NonNull[bool]
	imageUrl: Optional[str]
	nominationName: NonNull[str]
	year: NonNull[int]
	persons: list[AwardPerson] = []

	def add_person(self, person: Union[AwardPerson, list[AwardPerson]]):
		if isinstance(person, list):
			self.persons.extend(person)
		else:
			self.persons.append(person)
