from enum import Enum


class ReviewOrder(Enum):
	DATE_ASC = 1
	DATE_DESC = 2
	USER_POSITIVE_RATING_ASC = 3
	USER_POSITIVE_RATING_DESC = 4
	USER_NEGATIVE_RATING_ASC = 5
	USER_NEGATIVE_RATING_DESC = 6