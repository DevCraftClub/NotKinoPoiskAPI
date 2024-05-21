from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Enums.Sex import Sex


@dataclass
class PersonShort:
	"""
	Объект сотрудника фильма или сериала при поисковом запросе с краткой информацией
	:param kinopoiskId: Уникальный идентификатор сотрудника
	:param webUrl: Ссылка на страницу сотрудника
	:param nameRu: Имя на русском языке
	:param nameEn: Имя на английском языке
	:param sex: Пол сотрудника
	:param posterUrl: Фото сотрудника
	"""
	kinopoiskId: Optional[int]
	webUrl: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: Optional[str]

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
