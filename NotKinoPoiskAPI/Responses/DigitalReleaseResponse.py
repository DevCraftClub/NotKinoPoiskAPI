from typing import Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Types.DigitalReleaseItem import DigitalReleaseItem


@dataclass
class DigitalReleaseResponse:
	page: int
	total: int
	releases: list[DigitalReleaseItem] = field(default_factory=list)

	def add_release(self, release: Union[DigitalReleaseItem, list[DigitalReleaseItem]]):
		if isinstance(release, list):
			self.releases.extend(release)
		else:
			self.releases.append(release)
