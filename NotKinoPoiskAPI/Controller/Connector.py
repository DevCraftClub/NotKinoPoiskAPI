from dataclasses import dataclass
from typing import Optional

from requests import Session

from NotKinoPoiskAPI.Types.ProxyItem import ProxyItem


@dataclass
class Connector:
	headers: dict
	method: str
	url: str
	proxy: Optional[ProxyItem]
	session: Optional[Session]
	user_agent: Optional[str]

	def __post_init__(self):
		if Session is None:
			self.session = Session()
