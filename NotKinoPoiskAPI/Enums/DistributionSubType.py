from enum import Enum


class DistributionSubType(Enum):
	""" Подтипы дистрибуции """
	DVD = 'DVD'
	"""DVD"""
	DIGITAL = 'Цифровое издание'
	"""Цифровое издание"""
	BLURAY = 'BluRay'
	"""BluRay"""
	CINEMA = 'Кинотеатр'
	"""Кинотеатр"""
