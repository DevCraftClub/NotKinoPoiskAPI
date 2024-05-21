from paprika import NonNull, data


@data
class BoxOffice:
	type: NonNull[str]
	amount: NonNull[int]
	currencyCode: NonNull[str]
	name: NonNull[str]
	symbol: NonNull[str]
