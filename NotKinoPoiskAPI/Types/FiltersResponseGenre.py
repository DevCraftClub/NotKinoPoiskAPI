from dataclasses import dataclass

from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class FiltersResponseGenre(Genre):
	id: int
