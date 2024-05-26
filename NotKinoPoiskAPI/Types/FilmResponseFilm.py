from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.RelationType import RelationType


@dataclass
class FilmResponseFilm:
	"""
	:param filmId: ID фильма
	:param nameRu: русское название
	:param nameEn: английское название
	:param nameOriginal: оригинальное название
	:param posterUrl: ссылка на постер
	:param posterUrlPreview: ссылка на превью постера
	:param relationType: тип связи
	"""
	filmId: int
	nameRu: str
	nameEn: str
	nameOriginal: str
	posterUrl: str
	posterUrlPreview: str
	relationType: RelationType

	def __post_init__(self):
		if isinstance(self.relationType, str):
			self.relationType = ObjectController.find_enum(self.relationType, RelationType)

	def __str__(self):
		title = self.nameRu
		title += f" / {self.nameEn}" if self.nameEn else ""
		title += f" / {self.nameOriginal}" if self.nameOriginal else ""

		return str(title).strip()
