from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Sex import Sex


@data
class PersonByNameResponseItem:
	kinopoiskId: NonNull[int]
	webUrl: NonNull[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: NonNull[str]
