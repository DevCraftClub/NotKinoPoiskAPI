from dataclasses import dataclass
from typing import Optional


@dataclass
class ExternalSourceResponseItem:
	"""
	Класс для хранения информации о внешнем источнике.
	"""
	url: str
	"""Ссылка на источник"""
	platform: str
	"""Платформа"""
	logoUrl: str
	"""Ссылка на логотип"""
	positiveRating: int
	"""Положительный рейтинг"""
	negativeRating: int
	"""Отрицательный рейтинг"""
	author: str
	"""Автор"""
	title: Optional[str]
	"""Название"""
	description: str
	"""Описание"""
