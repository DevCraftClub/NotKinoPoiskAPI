from paprika import NonNull, data


@data
class Company:
	name: NonNull[str]
