from dataclasses import dataclass
from typing import Optional


@dataclass
class ExternalSourceResponseItem:
	"""
	Класс для хранения информации о внешнем источнике.
	:param url: Ссылка на источник.
	:param platform: Платформа.
	:param logoUrl: Ссылка на логотип.
	:param positiveRating: Положительный рейтинг.
	:param negativeRating: Отрицательный рейтинг.
	:param author: Автор.
	:param title: Название.
	:param description: Описание.
	"""
	url: str
	platform: str
	logoUrl: str
	positiveRating: int
	negativeRating: int
	author: str
	title: Optional[str]
	description: str
