from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.ReviewType import ReviewType


@data
class ReviewResponseItem:
	kinopoiskId: NonNull[int]
	type: NonNull[ReviewType]
	date: NonNull[str]
	positiveRating: NonNull[int]
	negativeRating: NonNull[int]
	author: NonNull[str]
	title: Optional[str]
	description: NonNull[str]
