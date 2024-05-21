from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.RelationType import RelationType
from NotKinoPoiskAPI.Types.FilmResponseFilm import FilmResponseFilm


@data
class FilmSequelsAndPrequelsResponse(FilmResponseFilm):
	"""
	Класс для хранения информации о продолжениях и предысториях фильма.
	:param filmId: ID фильма
	:param nameRu: русское название
	:param nameEn: английское название
	:param nameOriginal: оригинальное название
	:param posterUrl: ссылка на постер
	:param posterUrlPreview: ссылка на превью постера
	:param relationType: тип связи
	"""