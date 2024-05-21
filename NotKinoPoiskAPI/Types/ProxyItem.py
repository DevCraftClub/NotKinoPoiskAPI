from dataclasses import dataclass

from NotKinoPoiskAPI.Enums.ProxyType import ProxyType


@dataclass
class ProxyItem:
	"""
	Класс для хранения информации о прокси.
	:param ip: IP адрес прокси.
	:param port: Порт прокси.
	:param login: Логин прокси.
	:param password: Пароль прокси.
	:param type: Тип прокси.
	"""
	ip: str
	port: int
	login: str
	password: str
	type: ProxyType
