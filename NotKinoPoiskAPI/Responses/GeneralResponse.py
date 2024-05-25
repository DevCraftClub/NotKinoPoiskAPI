from dataclasses import dataclass, field
from typing import List


@dataclass
class GeneralResponse:
	"""
	Объект ответа
	:param total: Количество найденных объектов
	:param items: Список найденных объектов
	"""
	total: int
	totalPages: int = field(default_factory=int, init=False)
	items: List = field(default_factory=list, init=False)

	def __post_init__(self):
		if self.items is None:
			self.items = list()
