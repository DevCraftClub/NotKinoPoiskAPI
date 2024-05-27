from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.ReviewResponseItem import ReviewResponseItem


@dataclass
class ReviewResponse:
	"""
	Класс для хранения информации о рецензиях.
	"""
	total: int
	"""Общее количество рецензий"""
	totalPages: int
	"""Количество страниц"""
	totalPositiveReviews: int
	"""Количество положительных рецензий"""
	totalNegativeReviews: int
	"""Количество отрицательных рецензий"""
	totalNeutralReviews: int
	"""Количество нейтральных рецензий"""
	items: List[ReviewResponseItem] = field(default_factory=list)
	"""Список рецензий"""

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, ReviewResponseItem)

	def add_items(self, items: Union[ReviewResponseItem, List[ReviewResponseItem]]):
		"""
		Добавление рецензий

		:param Union[ReviewResponseItem, List[ReviewResponseItem]] items: Рецензия или список рецензий
		"""
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
