from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.FactType import FactType


@data
class Fact:
	text: NonNull[str]
	type: NonNull[FactType]
	spoiler: NonNull[bool] = False
	