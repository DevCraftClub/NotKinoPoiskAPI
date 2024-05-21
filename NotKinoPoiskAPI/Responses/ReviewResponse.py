from typing import Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Types.ReviewResponseItem import ReviewResponseItem


@data
class ReviewResponse:
	total: NonNull[int]
	totalPages: NonNull[int]
	totalPositiveReviews: NonNull[int]
	totalNegativeReviews: NonNull[int]
	totalNeutralReviews: NonNull[int]
	items: list[ReviewResponseItem] = []

	def add_items(self, items: Union[ReviewResponseItem,list[ReviewResponseItem]]):
		if isinstance(items, list):
			self.items.extend(items)
		else:
			self.items.append(items)

