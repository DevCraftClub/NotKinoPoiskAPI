from typing import Union, List

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.ReviewResponseItem import ReviewResponseItem


@dataclass
class ReviewResponse:
	total: int
	totalPages: int
	totalPositiveReviews: int
	totalNegativeReviews: int
	totalNeutralReviews: int
	items: List[ReviewResponseItem] = field(default_factory=list)

	def __post_init__(self):
		self.items = ObjectController.list_to_object(self.items, ReviewResponseItem)

	def add_items(self, items: Union[ReviewResponseItem, List[ReviewResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)
