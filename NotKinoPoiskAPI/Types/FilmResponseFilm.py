from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.RelationType import RelationType


@dataclass
class FilmResponseFilm:
	"""
	Класс для хранения информации о фильме.
	"""
	filmId: int
	"""ID фильма"""
	nameRu: str
	"""русское название"""
	nameEn: str
	"""английское название"""
	nameOriginal: str
	"""оригинальное название"""
	posterUrl: str
	"""ссылка на постер"""
	posterUrlPreview: str
	"""ссылка на превью постера"""
	relationType: RelationType
	"""тип связи"""

	def __post_init__(self):
		if isinstance(self.relationType, str):
			self.relationType = ObjectController.find_enum(self.relationType, RelationType)

	def __str__(self):
		title = self.nameRu
		title += f" / {self.nameEn}" if self.nameEn else ""
		title += f" / {self.nameOriginal}" if self.nameOriginal else ""

		return str(title).strip()
