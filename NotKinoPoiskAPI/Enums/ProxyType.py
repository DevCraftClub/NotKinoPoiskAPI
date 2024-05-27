from enum import Enum


class ProxyType(Enum):
	"""Типы прокси"""
	HTTP = 'http'
	"""HTTP"""
	HTTPS = 'https'
	"""HTTPS"""
	SOCKS4 = 'socks4'
	"""SOCKS4"""
	SOCKS5 = 'socks5'
	"""SOCKS5"""
