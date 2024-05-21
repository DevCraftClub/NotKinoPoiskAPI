from dataclasses import dataclass, field
from random import choice
from typing import Optional, Union

from decouple import config

from NotKinoPoiskAPI.Types.ProxyItem import ProxyItem


@dataclass
class ProxyController:
	proxy: list[ProxyItem] = field(default_factory=list)

	def __init__(self, proxy_data: Optional[Union[str, ProxyItem, list[ProxyItem]]] = None):
		if proxy_data is None:
			proxy_data = config.get('NKPA_PROXY', default=None, cast=str)

		if isinstance(proxy_data, str):
			self.add_proxy([ProxyItem(p) for p in proxy_data.split('||')])
		else:
			self.add_proxy(proxy_data)

	def add_proxy(self, proxy: Union[str, ProxyItem, list[ProxyItem]]):
		if isinstance(proxy, ProxyItem):
			self.proxy.append(proxy)
		else:
			self.proxy.extend(proxy)

	def get_random_proxy(self) -> ProxyItem | None:
		if len(self.proxy) == 0:
			return None
		return choice(self.proxy)
