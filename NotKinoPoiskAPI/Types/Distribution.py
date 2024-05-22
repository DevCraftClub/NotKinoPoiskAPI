from typing import Optional, Union

from dataclasses import dataclass, field

from NotKinoPoiskAPI.Enums.DistributionSubType import DistributionSubType
from NotKinoPoiskAPI.Enums.DistributionType import DistributionType
from NotKinoPoiskAPI.Types.Company import Company
from NotKinoPoiskAPI.Types.Country import Country


@dataclass
class Distribution:
	type: DistributionType
	subType: Optional[DistributionSubType]
	date: Optional[str]
	reRelease: Optional[bool]
	country: Optional[Country]
	companies: list[Company] = field(default_factory=list)

	def add_company(self, company: Union[Company, list[Company]]):
		if isinstance(company, list):
			self.companies.extend(company)
		else:
			self.companies.append(company)
