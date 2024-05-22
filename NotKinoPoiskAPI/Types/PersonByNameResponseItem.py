from typing import Optional

from dataclasses import dataclass

from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonByNameResponseItem:
	kinopoiskId: int
	webUrl: str
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: str
