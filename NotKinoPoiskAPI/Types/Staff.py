from typing import Optional

from NotKinoPoiskAPI.Enums.Profession import Profession


class Staff:
	"""
	Объект участников съёмок фильма или сериала. Данные выводятся в виде списка.
	Соответствует JSON-объекту: /api/v1/staff
	"""
	staffId: Optional[int]
	nameRu: Optional[str]
	nameEn: Optional[str]
	description: Optional[str]
	posterUrl: Optional[str]
	professionText: Optional[str]
	professionKey: Optional[Profession]

	def __init__(self, staffId: Optional[int] = None, nameRu: Optional[str] = None, nameEn: Optional[str] = None, description: Optional[str] = None, posterUrl: Optional[str] = None, professionText: Optional[str] = None, professionKey: Optional[Profession] = None):
		"""
			:param staffId (Optional[int]): Универсальный ID сотрудника.
			:param nameRu (Optional[str]): Имя на русском языке.
			:param nameEn (Optional[str]): Имя на английском языке.
			:param description (Optional[str]): Небольшое описание сотрудника.
			:param posterUrl (Optional[str]): Фотография сотрудника.
			:param professionText (Optional[str]): Роль в съёмках
			:param professionKey (Optional[str]): Ключ роли в съёмках
		"""
		self.staffId = staffId
		self.nameRu = nameRu
		self.nameEn = nameEn
		self.description = description
		self.posterUrl = posterUrl
		self.professionText = professionText
		self.professionKey = professionKey

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
