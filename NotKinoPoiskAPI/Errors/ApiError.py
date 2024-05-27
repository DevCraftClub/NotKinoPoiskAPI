from dataclasses import dataclass
from typing import Optional


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

		:param int code: Код ошибки
		:return: Описание ошибки
		:rtype: str
		"""
		error_codes = {
				401: "Пустой или неправильный токен",
				402: "Превышен лимит запросов(или дневной, или общий)",
				404: "Фильм не найден",
				429: "Слишком много запросов. Общий лимит - 20 запросов в секунду",
		}

		return error_codes.get(code, "Неизвестная ошибка")
