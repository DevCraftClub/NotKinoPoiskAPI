from dataclasses import dataclass


@dataclass
class ImageResponseItem:
	"""
	Класс для хранения информации об изображении.
	"""
	imageUrl: str
	"""Ссылка на изображение"""
	previewUrl: str
	"""Ссылка на превью изображения"""
