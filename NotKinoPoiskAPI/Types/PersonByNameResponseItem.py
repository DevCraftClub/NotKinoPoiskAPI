from typing import Optional

from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonByNameResponseItem:
	kinopoiskId: int
	webUrl: str
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: str

	def __post_init__(self):
		if self.sex is not None and isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)
