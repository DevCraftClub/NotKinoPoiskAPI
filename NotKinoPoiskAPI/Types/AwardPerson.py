from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Sex import Sex


@data
class AwardPerson:
	kinopoiskId: NonNull[int]
	webUrl: NonNull[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: NonNull[Sex]
	posterUrl: NonNull[str]
	growth: Optional[int]
	birthday: Optional[str]
	death: Optional[str]
	age: Optional[int]
	birthplace: Optional[str]
	deathplace: Optional[str]
	profession: Optional[str]
