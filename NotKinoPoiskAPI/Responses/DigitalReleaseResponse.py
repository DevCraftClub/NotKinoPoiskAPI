from typing import Union, List

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.DigitalReleaseItem import DigitalReleaseItem


@dataclass
class DigitalReleaseResponse:
	page: int
	total: int
	releases: List[DigitalReleaseItem] = field(default_factory=list)

	def __post_init__(self):
		self.releases = ObjectController.list_to_object(self.releases, DigitalReleaseItem)

	def add_release(self, release: Union[DigitalReleaseItem, list[DigitalReleaseItem]]):
		if isinstance(release, list):
			self.releases.extend(release)
		else:
			self.releases.append(release)
