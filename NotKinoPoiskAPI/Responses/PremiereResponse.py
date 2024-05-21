from dataclasses import dataclass, field

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse
from NotKinoPoiskAPI.Types.PremiereResponseItem import PremiereResponseItem


@dataclass
class PremiereResponse(GeneralResponse):
	"""
	Класс для хранения информации о премьере.
	:param total: Количество премьер.
	:param items: Список премьер.
	"""
	items: list[PremiereResponseItem] = field(default_factory=list)
