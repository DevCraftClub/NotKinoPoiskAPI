from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.DigitalReleaseItem import DigitalReleaseItem


@data
class DigitalReleaseResponse:
	page: NonNull[int]
	total: NonNull[int]
	releases: list[DigitalReleaseItem] = []

	def add_release(self, release: Union[DigitalReleaseItem, list[DigitalReleaseItem]]):
		if isinstance(release, list):
			self.releases.extend(release)
		else:
			self.releases.append(release)
