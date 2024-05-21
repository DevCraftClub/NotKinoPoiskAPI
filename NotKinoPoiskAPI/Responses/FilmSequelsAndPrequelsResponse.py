from paprika import NonNull, data


@data
class FilmSequelsAndPrequelsResponse:
	filmId: NonNull[int]
	