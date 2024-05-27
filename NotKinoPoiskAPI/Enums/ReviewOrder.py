from enum import Enum


class ReviewOrder(Enum):
	"""Типы порядка сортировки отзывов"""
	DATE_ASC = 1
	"""По дате"""
	DATE_DESC = 2
	"""По дате в обратном порядке"""
	USER_POSITIVE_RATING_ASC = 3
	"""По положительной оценке пользователя"""
	USER_POSITIVE_RATING_DESC = 4
	"""По положительной оценке пользователя в обратном порядке"""
	USER_NEGATIVE_RATING_ASC = 5
	"""По отрицательной оценке пользователя"""
	USER_NEGATIVE_RATING_DESC = 6
	"""По отрицательной оценке пользователя в обратном порядке"""
