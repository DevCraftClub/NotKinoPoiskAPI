from dataclasses import dataclass, field
from random import choice
from typing import Optional, Union

from decouple import config

from NotKinoPoiskAPI.Types.ProxyItem import ProxyItem


@dataclass
class ProxyController:
	"""
	Класс для работы с прокси
	"""
	proxy_list: list[ProxyItem] = field(default_factory=list)
	"""Список прокси"""

	def __init__(self, proxy_data: Optional[Union[str, ProxyItem, list[ProxyItem]]] = None):
		"""
		Инициализация

		Args:
			proxy_data (Optional[Union[str, ProxyItem, List[.ProxyItem]]]): Данные для добавления прокси. Либо необработанной строкой, либо списком или самим объектом прокси
		"""
		if proxy_data is None:
			proxy_data = config('NKPA_PROXY', default=None, cast=str)
			if proxy_data == 'None': proxy_data = None

		if proxy_data is not None:
			if isinstance(proxy_data, str):
				self.add_proxy([ProxyItem(p) for p in proxy_data.split('||')])
			else:
				self.add_proxy(proxy_data)

	def add_proxy(self, proxy: Union[str, ProxyItem, list[ProxyItem]]):
		"""
		Добавление прокси

		Args:
			proxy (Union[str, ProxyItem, List[ProxyItem]]): Строка, объект или список объектов прокси
		"""
		if isinstance(proxy, ProxyItem):
			self.proxy_list.append(proxy)
		else:
			self.proxy_list.extend(proxy)

	def get_proxy_list(self) -> list[ProxyItem]:
		"""
		Получение списка прокси

		Returns:
			List[ProxyItem]: Возвращает список прокси
		"""
		try:
			return self.proxy_list
		except Exception as _:
			self.proxy_list: list[ProxyItem] = []
			return self.proxy_list

	def get_random_proxy(self) -> ProxyItem | None:
		"""
		Получение случайного прокси

		Returns:
			ProxyItem or None: Получение случайного прокси
		"""
		if len(self.get_proxy_list()) == 0:
			return None
		return choice(self.get_proxy_list())
