from paprika import NonNull, data

from NotKinoPoiskAPI.Types.Country import Country


@data
class FiltersResponseCountry(Country):
	id: NonNull[int]
