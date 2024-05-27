from enum import Enum


class VideoResponseItemSite(Enum):
	"""Сайты видео"""
	YOUTUBE = 'YouTube'
	"""Ссылка на YouTube"""
	KINOPOISK_WIDGET = 'KinoPoiskWidget'
	"""Видео из виджета КиноПоиска"""
	YANDEX_DISK = 'YandexDisk'
	"""Ссылка на Яндекс.Диск"""
	UNKNOWN = 'Неизвестно'
	"""Неизвестно"""
