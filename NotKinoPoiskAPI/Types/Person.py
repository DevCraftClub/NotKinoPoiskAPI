from typing import Optional, Union

from NotKinoPoiskAPI.Enums.Sex import Sex
from NotKinoPoiskAPI.Types.FilmShort import FilmShort
from NotKinoPoiskAPI.Types.Spouse import Spouse


class Person:
	"""
	Объект конкретного сотрудника фильма или сериала с более подробной информацией
	"""
	personId: Optional[int]
	webUrl: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: Optional[str]
	growth: Optional[str]
	birthday: Optional[str]
	death: Optional[str]
	age: Optional[int]
	birthplace: Optional[str]
	deathplace: Optional[str]
	hasAwards: int = 0
	profession: Optional[str]
	facts: list[str] = []
	spouses: list[Spouse] = []
	films: list[FilmShort] = []

	def __init__(self, personId: Optional[int] = None, webUrl: Optional[str] = None, nameRu: Optional[str] = None,
				 nameEn: Optional[str] = None, sex: Optional[Sex] = None, posterUrl: Optional[str] = None,
				 growth: Optional[str] = None, age: Optional[int] = None, birthplace: Optional[str] = None,
				 deathplace: Optional[str] = None, hasAwards: int = 0, profession: Optional[str] = None,
				 facts=None, spouses=None, films=None):
		"""

		:param personId: Уникальный идентификатор сотрудника
		:param webUrl: Ссылка на страницу сотрудника
		:param nameRu: Имя сотрудника на русском языке
		:param nameEn: Имя на английском языке
		:param sex: Пол сотрудника
		:param posterUrl: Фото сотрудника
		:param growth: Рост сотрудника
		:param age: Возраст сотрудника
		:param birthplace: Место рождения
		:param deathplace: Место смерти
		:param hasAwards: Количество наград
		:param profession: Основной род деятельности
		:param facts: Факты о сотруднике
		:param spouses: Супруги сотрудника
		:param films: Фильмография
		"""
		if films is None:
			films = []
		if spouses is None:
			spouses = []
		if facts is None:
			facts = []

		self.personId = personId
		self.webUrl = webUrl
		self.nameRu = nameRu
		self.nameEn = nameEn
		self.sex = sex
		self.posterUrl = posterUrl
		self.growth = growth
		self.age = age
		self.birthplace = birthplace
		self.deathplace = deathplace
		self.hasAwards = hasAwards
		self.profession = profession
		self.facts = facts
		self.spouses = spouses
		self.films = films

	def add_fact(self, fact: Union[str, list[str]]):
		"""
		Добавляет факт о сотруднике.
		:param fact: Факт о сотруднике. Допустимы список или строка
		"""
		if isinstance(fact, str):
			self.facts.append(fact)
		else:
			self.facts.extend(fact)

	def add_spouse(self, spouse: Union[Spouse, list[Spouse]]):
		"""
		Добавляет супругу сотрудника.
		:param spouse: Супруга сотрудника. Допустимы список с объектами Spouse или сам объект Spouse
		"""
		if isinstance(spouse, Spouse):
			self.spouses.append(spouse)
		else:
			self.spouses.extend(spouse)

	def add_film(self, film: Union[FilmShort, list[FilmShort]]):
		"""
		Добавляет фильм сотрудника.
		:param film: Фильм сотрудника. Допустимы список с объектами FilmShort или сам объект FilmShort
		"""
		if isinstance(film, FilmShort):
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
