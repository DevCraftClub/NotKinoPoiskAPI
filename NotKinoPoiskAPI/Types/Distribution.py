from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.DistributionSubType import DistributionSubType
from NotKinoPoiskAPI.Enums.DistributionType import DistributionType
from NotKinoPoiskAPI.Types.Company import Company
from NotKinoPoiskAPI.Types.Country import Country


@data
class Distribution:
	type: NonNull[DistributionType]
	subType: Optional[DistributionSubType]
	date: Optional[str]
	reRelease: Optional[bool]
	country: Optional[Country]
	companies: list[Company] = []

	def add_company(self, company: Union[Company, list[Company]]):
		if isinstance(company, list):
			self.companies.extend(company)
		else:
			self.companies.append(company)
