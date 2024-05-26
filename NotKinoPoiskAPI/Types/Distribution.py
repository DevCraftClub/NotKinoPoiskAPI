from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
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
	companies: List[Company] = field(default_factory=list)

	def __post_init__(self):
		self.companies = ObjectController.list_to_object(self.companies, Company)
		if self.country is not None and isinstance(self.country, str): self.country = ObjectController.json_to_object(
			self.country, Country)

		if isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, DistributionType)

		if self.subType is not None and isinstance(self.subType, str):
			self.subType = ObjectController.find_enum(self.subType, DistributionSubType)

	def add_company(self, company: Union[Company, list[Company]]):
		if isinstance(company, list):
			self.companies.extend(company)
		else:
			self.companies.append(company)
