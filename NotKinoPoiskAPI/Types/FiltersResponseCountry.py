from dataclasses import dataclass

from NotKinoPoiskAPI.Types.Country import Country


@dataclass
class FiltersResponseCountry(Country):
	"""
	Класс для хранения информации о стране.
	"""
	id: int
	"""ID страны"""
