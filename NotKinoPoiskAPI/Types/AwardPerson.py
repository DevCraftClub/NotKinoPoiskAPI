from typing import Optional

from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class AwardPerson:
	kinopoiskId: int
	webUrl: str
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Sex
	posterUrl: str
	growth: Optional[int]
	birthday: Optional[str]
	death: Optional[str]
	age: Optional[int]
	birthplace: Optional[str]
	deathplace: Optional[str]
	profession: Optional[str]

	def __post_init__(self):
		if isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)
