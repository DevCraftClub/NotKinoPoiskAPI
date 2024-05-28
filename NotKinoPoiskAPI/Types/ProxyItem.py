from typing import Optional

from NotKinoPoiskAPI.Enums.ProxyType import ProxyType


class ProxyItem:
	"""
	Класс для хранения информации о прокси.
	"""
	ip: str
	"""IP адрес прокси"""
	port: int
	"""Порт прокси"""
	login: str
	"""Логин прокси"""
	password: str
	"""Пароль прокси"""
	type: ProxyType
	"""Тип прокси"""
	proxy_set: bool = False
	"""Установлен ли прокси"""

	def __init__(self, proxy_string: Optional[str] = None):
		"""
		Инициализация прокси

		Args:
			proxy_string (Optional[str], optional): Строка прокси. Если параметр пуст, то скрипт берёт данные из .env. По умолчанию None.
		"""
		if proxy_string is not None:
			proxy_type, proxy_address = proxy_string.split('|')
			self.type = ProxyType(proxy_type.upper())

			if '@' in proxy_address:
				login, password, ip_address = proxy_address.split('@')
				ip, port = ip_address.split(':')
				self.login = login
				self.password = password
			else:
				ip, port = proxy_address.split(':')

			self.ip = ip
			self.port = int(port) if ':' in port else 80
			self.proxy_set = True

	def __str__(self):
		user = f"{self.login}:{self.password}@" if self.login is not None and self.password is not None else ""
		return f"{user}{self.ip}:{self.port}"
