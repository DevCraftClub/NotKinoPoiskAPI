from dataclasses import dataclass

from NotKinoPoiskAPI.Enums.FactType import FactType


@dataclass
class Fact:
	text: str
	type: FactType
	spoiler: bool = False
	