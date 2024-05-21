from typing import Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Types.ReviewResponseItem import ReviewResponseItem


@dataclass
class ReviewResponse:
	total: int
	totalPages: int
	totalPositiveReviews: int
	totalNegativeReviews: int
	totalNeutralReviews: int
	items: list[ReviewResponseItem] = field(default_factory=list)

	def add_items(self, items: Union[ReviewResponseItem,list[ReviewResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)

