from dataclasses import dataclass


@dataclass
class BoxOffice:
	type: str
	amount: int
	currencyCode: str
	name: str
	symbol: str
