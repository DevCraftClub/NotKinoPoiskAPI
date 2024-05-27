from dataclasses import dataclass
from typing import Optional


@dataclass
class Episode:
	"""
	Объект эпизода
	"""
	seasonNumber: int
	"""Номер сезона"""
	episodeNumber: int
	"""Номер эпизода"""
	nameRu: str
	"""Название эпизода"""
	nameEn: Optional[str]
	"""Название эпизода на английском"""
	synopsis: Optional[str]
	"""Краткое содержание эпизода"""
	releaseDate: Optional[str]
	"""Дата выхода"""

	def __str__(self):
		"""
		Выводит отформатировано название эпизода.
		"""

		return f"S{str(self.seasonNumber).zfill(2)}E{str(self.episodeNumber).zfill(2)}"
