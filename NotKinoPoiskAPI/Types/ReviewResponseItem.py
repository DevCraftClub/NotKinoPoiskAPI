from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.ReviewType import ReviewType


@dataclass
class ReviewResponseItem:
	"""
	Объект отзыва
	"""
	kinopoiskId: int
	"""Идентификатор фильма"""
	type: ReviewType
	"""Тип отзыва"""
	date: str
	"""Дата отзыва"""
	positiveRating: int
	"""Количество положительных оценок"""
	negativeRating: int
	"""Количество отрицательных оценок"""
	author: str
	"""Автор отзыва"""
	title: Optional[str]
	"""Заголовок отзыва"""
	description: str
	"""Текст отзыва"""

	def __post_init__(self):
		if isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, ReviewType)
