from enum import Enum


class RelationType(Enum):
	SEQUEL = "Сиквел"
	"""Сиквел"""
	PREQUEL = "Приквел"
	"""Приквел"""
	REMAKE = "Римейк"
	"""Римейк"""
	UNKNOWN = "Неизвестно"
	"""Неизвестно"""
	SIMILAR = "Похожий"
	"""Похожий"""
