from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.ErrorCode import ErrorCode


@dataclass
class ApiError:
	"""
	Класс для хранения информации об ошибке.
	"""
	message: str
	"""Сообщение об ошибке"""

	@staticmethod
	def get_error_description(code: int):
		"""
		Метод для получения описания ошибки по коду.

		Args:
			code (int): Код ошибки

		Returns:
			str: Описание ошибки
		"""
		error_code = f'E{code}'
		if error_code in ErrorCode.get_names():
			code_descr = ObjectController.find_enum(error_code, ErrorCode)
		else:
			code_descr = "Неизвестная ошибка"

		return code_descr
