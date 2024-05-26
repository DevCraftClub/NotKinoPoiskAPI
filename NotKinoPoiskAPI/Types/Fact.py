from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.FactType import FactType


@dataclass
class Fact:
	text: str
	type: FactType
	spoiler: bool = False

	def __post_init__(self):
		if self.type is not None and isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, FactType)
