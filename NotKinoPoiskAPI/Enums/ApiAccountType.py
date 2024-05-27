from enum import Enum


class ApiAccountType(Enum):
	"""Тип аккаунта"""
	FREE = "Бесплатный"
	"""Бесплатный"""
	EXTENDED = "Расширенный"
	"""Расширенный"""
	UNLIMITED = "Безлимитный"
	"""Безлимитный"""
