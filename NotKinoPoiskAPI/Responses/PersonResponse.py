from typing import Optional, Union

from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.Sex import Sex
from NotKinoPoiskAPI.Responses.PersonResponseFilms import PersonResponseFilms
from NotKinoPoiskAPI.Responses.PersonResponseSpouse import PersonResponseSpouse


@data
class PersonResponse:
	"""
	Объект конкретного сотрудника фильма или сериала с более подробной информацией
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
	personId: NonNull[int]
	webUrl: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	sex: Optional[Sex]
	posterUrl: NonNull[str]
	growth: Optional[str]
	birthday: Optional[str]
	death: Optional[str]
	age: Optional[int]
	birthplace: Optional[str]
	deathplace: Optional[str]
	hasAwards: int = 0
	profession: Optional[str]
	facts: list[str] = []
	spouses: list[PersonResponseSpouse] = []
	films: list[PersonResponseFilms] = []

	def add_fact(self, fact: Union[str, list[str]]):
		"""
		Добавляет факт о сотруднике.
		:param fact: Факт о сотруднике. Допустимы список или строка
		"""
		if isinstance(fact, str):
			self.facts.append(fact)
		else:
			self.facts.extend(fact)

	def add_spouse(self, spouse: Union[PersonResponseSpouse, list[PersonResponseSpouse]]):
		"""
		Добавляет супругу сотрудника.
		:param spouse: Супруга сотрудника. Допустимы список с объектами Spouse или сам объект Spouse
		"""
		if isinstance(spouse, PersonResponseSpouse):
			self.spouses.append(spouse)
		else:
			self.spouses.extend(spouse)

	def add_film(self, film: Union[PersonResponseFilms, list[PersonResponseFilms]]):
		"""
		Добавляет фильм сотрудника.
		:param film: Фильм сотрудника. Допустимы список с объектами FilmShort или сам объект FilmShort
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