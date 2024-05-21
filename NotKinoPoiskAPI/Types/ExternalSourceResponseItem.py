from typing import Optional
from paprika import NonNull, data


@data
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
	url: NonNull[str]
	platform: NonNull[str]
	logoUrl: NonNull[str]
	positiveRating: NonNull[int]
	negativeRating: NonNull[int]
	author: NonNull[str]
	title: Optional[str]
	description: NonNull[str]
