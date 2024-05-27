from dataclasses import dataclass


@dataclass
class BoxOffice:
	"""
	Класс для хранения информации о кассовых сборах.
	"""
	type: str
	"""Тип"""
	amount: int
	"""Сумма"""
	currencyCode: str
	"""Код валюты"""
	name: str
	"""Название валюты"""
	symbol: str
	"""Символ валюты"""
