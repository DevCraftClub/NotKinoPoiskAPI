from paprika import NonNull, data

from NotKinoPoiskAPI.Types.Genre import Genre


@data
class FiltersResponseGenre(Genre):
	id: NonNull[int]
