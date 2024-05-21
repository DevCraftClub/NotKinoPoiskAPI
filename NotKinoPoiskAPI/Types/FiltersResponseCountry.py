from dataclasses import dataclass

from NotKinoPoiskAPI.Types.Country import Country


@dataclass
class FiltersResponseCountry(Country):
	id: int
