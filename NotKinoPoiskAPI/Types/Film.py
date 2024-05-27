from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Enums.ProductionStatus import ProductionStatus
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@dataclass
class Film:
	"""
	Объект фильма или сериала
	"""
	kinopoiskId: int
	"""Идентификатор фильма"""
	kinopoiskHDId: Optional[str]
	"""Идентификатор фильма в КиноПоиск Онлайн"""
	imdbId: Optional[str]
	"""Идентификатор фильма на IMDB"""
	nameRu: Optional[str]
	"""Название фильма"""
	nameEn: Optional[str]
	"""Название фильма на английском"""
	nameOriginal: Optional[str]
	"""Оригинальное название фильма"""
	posterUrl: str
	"""Ссылка на постер"""
	posterUrlPreview: str
	"""Ссылка на превью постера"""
	coverUrl: Optional[str]
	"""Ссылка на обложку"""
	logoUrl: Optional[str]
	"""Ссылка на логотип"""
	ratingGoodReview: Optional[int]
	"""Рейтинг отзывов"""
	ratingGoodReviewVoteCount: Optional[int]
	"""Количество хороших отзывов"""
	ratingKinopoisk: Optional[float]
	"""Рейтинг КиноПоиск"""
	ratingKinopoiskVoteCount: Optional[int]
	"""Количество голосов за рейтинг КиноПоиск"""
	ratingImdb: Optional[float]
	"""Рейтинг IMDB"""
	ratingImdbVoteCount: Optional[int]
	"""Количество голосов за рейтинг IMDB"""
	ratingFilmCritics: Optional[float]
	"""Рейтинг критиков"""
	ratingFilmCriticsVoteCount: Optional[int]
	"""Количество голосов за рейтинг критиков"""
	ratingAwait: Optional[float]
	"""Рейтинг ожидания"""
	ratingAwaitCount: Optional[int]
	"""Количество голосов за рейтинг ожидания"""
	ratingRfCritics: Optional[float]
	"""Рейтинг критиков России"""
	ratingRfCriticsVoteCount: Optional[int]
	"""Количество голосов за рейтинг критиков России"""
	webUrl: str
	"""Ссылка на страницу фильма"""
	year: Optional[int]
	"""Год выпуска"""
	filmLength: Optional[int]
	"""Длительность фильма"""
	slogan: Optional[str]
	"""Слоган"""
	description: Optional[str]
	"""Описание"""
	shortDescription: Optional[str]
	"""Краткое описание"""
	editorAnnotation: Optional[str]
	"""Аннотация режиссера"""
	productionStatus: Optional[ProductionStatus]
	"""Статус производства"""
	type: Optional[MovieType]
	"""Тип медиа"""
	ratingMpaa: Optional[str]
	"""Рейтинг MPAA"""
	ratingAgeLimits: Optional[str]
	"""Возрастные ограничения"""
	hasImax: Optional[bool]
	"""Есть ли в IMAX"""
	has3D: Optional[bool]
	"""Есть ли в 3D"""
	lastSync: datetime
	"""Дата последнего обновления"""
	startYear: Optional[int]
	"""Год начала выпуска"""
	endYear: Optional[int]
	"""Год окончания выпуска"""
	serial: Optional[bool]
	"""Сериал"""
	shortFilm: Optional[bool]
	"""Короткометражка"""
	completed: Optional[bool]
	"""Завершен"""
	countries: List[Country] = field(default_factory=list)
	"""Страны"""
	genres: List[Genre] = field(default_factory=list)
	"""Жанры"""
	reviewsCount: int = 0
	"""Количество отзывов"""
	isTicketsAvailable: bool = False
	"""Доступны ли билеты"""

	def __post_init__(self):
		if self.countries is None:
			self.countries = list()
		else:
			self.countries = ObjectController.list_to_object(self.countries, Country)
		if self.genres is None:
			self.genres = list()
		else:
			self.genres = ObjectController.list_to_object(self.genres, Genre)
		if self.type is not None and isinstance(self.type, str):
			self.type = ObjectController.find_enum(self.type, MovieType)
		if self.productionStatus is not None and isinstance(self.productionStatus, str):
			self.productionStatus = ObjectController.find_enum(self.productionStatus, ProductionStatus)

	def add_country(self, country: Union[Country, list[Country]]):
		"""
		Добавление страны производства

		:param Union[Country, list[Country]] country: Страна или список стран
		"""
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)

	def add_genres(self, genres: Union[Genre, list[Genre]]):
		"""
		Добавление жанра

		:param Union[Genre, list[Genre]] genres: Жанр или список жанров
		"""
		if isinstance(genres, list):
			self.genres.extend(genres)
		else:
			self.genres.append(genres)

	def __str__(self):
		title = self.nameRu
		title += f" / {self.nameEn}" if self.nameEn else ""
		title += f" / {self.nameOriginal}" if self.nameOriginal else ""
		title += f" ({self.year})" if self.year else ""

		return title.strip()
