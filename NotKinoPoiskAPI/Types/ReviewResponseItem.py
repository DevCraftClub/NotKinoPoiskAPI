from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Enums.ReviewType import ReviewType


@dataclass
class ReviewResponseItem:
	kinopoiskId: int
	type: ReviewType
	date: str
	positiveRating: int
	negativeRating: int
	author: str
	title: Optional[str]
	description: str

	def __post_init__(self):
		self.type = ReviewType(self.type)
