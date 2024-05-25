from typing import Optional

from NotKinoPoiskAPI.Enums.ProxyType import ProxyType


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
	proxy_set: bool = False

	def __init__(self, proxy_string: Optional[str] = None):
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
