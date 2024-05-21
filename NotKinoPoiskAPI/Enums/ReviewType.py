from enum import Enum


class ReviewType(Enum):
	POSITIVE = "Положительный"
	NEGATIVE = "Отрицательный"
	NEUTRAL = "Нейтральный"
	UNKNOWN = "Неизвестно"
