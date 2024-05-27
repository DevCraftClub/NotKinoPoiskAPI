from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.DigitalReleaseItem import DigitalReleaseItem


@dataclass
class DigitalReleaseResponse:
	"""
	Объект ответа на поиск цифровых релизов
	"""
	page: int
	"""Номер страницы"""
	total: int
	"""Общее количество релизов"""
	releases: List[DigitalReleaseItem] = field(default_factory=list)
	"""Список найденных релизов"""

	def __post_init__(self):
		self.releases = ObjectController.list_to_object(self.releases, DigitalReleaseItem)

	def add_release(self, release: Union[DigitalReleaseItem, list[DigitalReleaseItem]]):
		"""
		Добавление релиза

		:param Union[DigitalReleaseItem, list[DigitalReleaseItem]] release: Релиз или список релизов
		"""
		if isinstance(release, list):
			self.releases.extend(release)
		else:
			self.releases.append(release)
