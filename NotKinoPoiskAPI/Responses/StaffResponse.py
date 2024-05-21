from typing import Optional

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Profession import Profession


@data
class StaffResponse:
	"""
	Объект участников съёмок фильма или сериала. Данные выводятся в виде списка.
	:param staffId (Optional[int]): Универсальный ID сотрудника.
	:param nameRu (Optional[str]): Имя на русском языке.
	:param nameEn (Optional[str]): Имя на английском языке.
	:param description (Optional[str]): Небольшое описание сотрудника.
	:param posterUrl (Optional[str]): Фотография сотрудника.
	:param professionText (Optional[str]): Роль в съёмках
	:param professionKey (Optional[str]): Ключ роли в съёмках
	"""
	staffId: NonNull[int]
	nameRu: Optional[str]
	nameEn: Optional[str]
	description: Optional[str]
	posterUrl: NonNull[str]
	professionText: NonNull[str]
	professionKey: NonNull[Profession]

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
