from typing import Optional

from dataclasses import dataclass


@dataclass
class ApiError:
	"""
	Класс для хранения информации об ошибке.
	:param message: Сообщение об ошибке.
	:param errorCode: Код ошибки.
	"""
	message: str
	errorCode: Optional[int]

	def get_error_description(self, code: int):
		"""
		Метод для получения описания ошибки по коду.
		"""
		error_codes = {
			401: "Пустой или неправильный токен",
			402: "Превышен лимит запросов(или дневной, или общий)",
			404: "Фильм не найден",
			429: "Слишком много запросов. Общий лимит - 20 запросов в секунду",
		}

		return error_codes.get(code, "Неизвестная ошибка")
