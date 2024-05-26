from dataclasses import dataclass
from typing import Optional

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Profession import Profession


@dataclass
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
	staffId: int
	nameRu: Optional[str]
	nameEn: Optional[str]
	description: Optional[str]
	posterUrl: str
	professionText: str
	professionKey: Profession

	def __post_init__(self):
		if isinstance(self.professionKey, str):
			self.professionText = ObjectController.find_enum(self.professionKey, Profession)

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
