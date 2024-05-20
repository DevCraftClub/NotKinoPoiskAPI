from typing import Optional

from NotKinoPoiskAPI.Enums.Sex import Sex


class PersonShort:
	"""
	Объект сотрудника фильма или сериала при поисковом запросе с краткой информацией
	"""
	kinopoiskId: Optional[int]
	webUrl: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: Optional[str]

	def __init__(self, kinopoiskId: Optional[int] = None, webUrl: Optional[str] = None, nameRu: Optional[str] = None, nameEn: Optional[str] = None, sex: Optional[Sex] = None, posterUrl: Optional[str] = None):
		"""
		:param kinopoiskId: Уникальный идентификатор сотрудника
		:param webUrl: Ссылка на страницу сотрудника
		:param nameRu: Имя на русском языке
		:param nameEn: Имя на английском языке
		:param sex: Пол сотрудника
		:param posterUrl: Фото сотрудника
		"""
		self.kinopoiskId = kinopoiskId
		self.webUrl = webUrl
		self.nameRu = nameRu
		self.nameEn = nameEn
		self.sex = sex
		self.posterUrl = posterUrl

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
