from dataclasses import dataclass, field
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.Sex import Sex
from NotKinoPoiskAPI.Responses.PersonResponseFilms import PersonResponseFilms
from NotKinoPoiskAPI.Responses.PersonResponseSpouse import PersonResponseSpouse


@dataclass
class PersonResponse:
	"""
	Объект конкретного сотрудника фильма или сериала с более подробной информацией
	"""
	personId: int
	"""Уникальный идентификатор сотрудника"""
	webUrl: Optional[str]
	"""Ссылка на страницу сотрудника"""
	nameRu: Optional[str]
	"""Имя сотрудника на русском языке"""
	nameEn: Optional[str]
	"""Имя на английском языке"""
	sex: Optional[Sex]
	"""Пол сотрудника"""
	posterUrl: str
	"""Фото сотрудника"""
	growth: Optional[str]
	"""Рост сотрудника"""
	birthday: Optional[str]
	"""Дата рождения сотрудника"""
	death: Optional[str]
	"""Дата смерти сотрудника"""
	age: Optional[int]
	"""Возраст сотрудника"""
	birthplace: Optional[str]
	"""Место рождения"""
	deathplace: Optional[str]
	"""Место смерти"""
	profession: Optional[str]
	"""Основной род деятельности"""
	hasAwards: int = 0
	"""Количество наград"""
	facts: List[str] = field(default_factory=list)
	"""Факты о сотруднике"""
	spouses: List[PersonResponseSpouse] = field(default_factory=list)
	"""Супруги сотрудника"""
	films: List[PersonResponseFilms] = field(default_factory=list)
	"""Фильмография"""

	def __post_init__(self):
		self.spouses = ObjectController.list_to_object(self.spouses, PersonResponseSpouse)
		self.films = ObjectController.list_to_object(self.films, PersonResponseFilms)
		if self.sex is not None and isinstance(self.sex, str):
			self.sex = ObjectController.find_enum(self.sex, Sex)

	def add_fact(self, fact: Union[str, list[str]]):
		"""
		Добавляет факт о сотруднике.

		Args:
			fact (Union[str, list[str]]): Факт о сотруднике. Допустимы список или строка
		"""
		if isinstance(fact, str):
			self.facts.append(fact)
		else:
			self.facts.extend(fact)

	def add_spouse(self, spouse: Union[PersonResponseSpouse, list[PersonResponseSpouse]]):
		"""
		Добавляет супругу сотрудника.

		Args:
			spouse (Union[PersonResponseSpouse, list[PersonResponseSpouse]]): Супруга сотрудника. Допустимы список с объектами Spouse или сам объект Spouse
		"""
		if isinstance(spouse, PersonResponseSpouse):
			self.spouses.append(spouse)
		else:
			self.spouses.extend(spouse)

	def add_film(self, film: Union[PersonResponseFilms, list[PersonResponseFilms]]):
		"""
		Добавляет фильм сотрудника.

		Args:
			film (Union[PersonResponseFilms, list[PersonResponseFilms]]): Фильм сотрудника. Допустимы список с объектами FilmShort или сам объект FilmShort
		"""
		if isinstance(film, PersonResponseFilms):
			self.films.append(film)
		else:
			self.films.extend(film)

	def __str__(self):
		"""
		Выводит отформатировано имя сотрудника.
		"""
		if self.nameEn and self.nameEn != self.nameRu:
			return f"{self.nameRu} ({self.nameEn})"

		return self.nameRu
