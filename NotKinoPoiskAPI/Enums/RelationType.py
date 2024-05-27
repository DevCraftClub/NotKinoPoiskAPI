from enum import Enum


class RelationType(Enum):
	"""Типы связей"""
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
