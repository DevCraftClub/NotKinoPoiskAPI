from paprika import data

from NotKinoPoiskAPI.Responses.GeneralResponse import GeneralResponse


@data
class PremiereResponse(GeneralResponse):
	"""
	Класс для хранения информации о премьере.
	:param total: Количество премьер.
	:param items: Список премьер.
	"""
	items: list = []