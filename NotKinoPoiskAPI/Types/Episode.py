from typing import Optional

from paprika import data, NonNull


@data
class Episode:
	"""
	Объект эпизода
	:param seasonNumber: Номер сезона
	:param episodeNumber: Номер эпизода
	:param nameRu: Название эпизода
	:param nameEn: Название эпизода на английском
	:param synopsis: Краткое содержание эпизода
	:param releaseDate: Краткое содержание эпизода
	"""
	seasonNumber: NonNull[int]
	episodeNumber: NonNull[int]
	nameRu: NonNull[str]
	nameEn: Optional[str]
	synopsis: Optional[str]
	releaseDate: Optional[str]

	def __str__(self):
		"""
		Выводит отформатировано название эпизода.
		"""

		return f"S{str(self.seasonNumber).zfill(2)}E{str(self.episodeNumber).zfill(2)}"
