from dataclasses import dataclass

from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class FiltersResponseGenre(Genre):
	"""
	Класс для хранения информации о жанре.
	"""
	id: int
	"""ID жанра"""
