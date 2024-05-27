from dataclasses import dataclass, field
from typing import List


@dataclass
class GeneralResponse:
	"""
	Объект ответа
	"""
	total: int
	"""Количество найденных объектов"""
	totalPages: int = field(default_factory=int, init=False)
	"""Количество страниц"""
	items: List = field(default_factory=list, init=False)
	"""Список найденных объектов"""

	def __post_init__(self):
		if self.items is None:
			self.items = list()
