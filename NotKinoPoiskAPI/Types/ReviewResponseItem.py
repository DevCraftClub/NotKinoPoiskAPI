from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
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
		if isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, ReviewType)
