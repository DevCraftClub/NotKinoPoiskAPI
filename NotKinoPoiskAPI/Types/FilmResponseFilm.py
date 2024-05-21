from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.RelationType import RelationType


@data
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
	filmId: NonNull[int]
	nameRu: NonNull[str]
	nameEn: NonNull[str]
	nameOriginal: NonNull[str]
	posterUrl: NonNull[str]
	posterUrlPreview: NonNull[str]
	relationType: NonNull[RelationType]

	def __str__(self):
		title = self.nameRu
		title += f" / {self.nameEn}" if self.nameEn else ""
		title += f" / {self.nameOriginal}" if self.nameOriginal else ""

		return str(title).strip()
