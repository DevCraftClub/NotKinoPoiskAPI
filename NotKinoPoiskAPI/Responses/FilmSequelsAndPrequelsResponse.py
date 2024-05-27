from dataclasses import dataclass

from NotKinoPoiskAPI.Types.FilmResponseFilm import FilmResponseFilm


@dataclass
class FilmSequelsAndPrequelsResponse(FilmResponseFilm):
	"""
	Класс для хранения информации о продолжениях и предысториях фильма.
	"""
