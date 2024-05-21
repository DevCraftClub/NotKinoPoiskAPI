from datetime import datetime
from typing import Optional, Union

from paprika import data, NonNull

from NotKinoPoiskAPI.Enums.ProductionStatus import ProductionStatus
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Types.Country import Country
from NotKinoPoiskAPI.Types.Genre import Genre


@data
class Film:
	"""
	Объект фильма или сериала
	:param kinopoiskId: Идентификатор фильма
	:param kinopoiskHDId: Идентификатор фильма в HD
	:param imdbId: Идентификатор фильма в IMDB
	:param nameRu: Название фильма
	:param nameEn: Название фильма (англ.)
	:param nameOriginal: Название фильма (оригинал)
	:param posterUrl: Ссылка на постер
	:param posterUrlPreview: Ссылка на постер
	:param coverUrl: Ссылка на обложку
	:param logoUrl: Ссылка на логотип
	:param reviewsCount: Количество отзывов
	:param ratingGoodReview: Рейтинг отзывов
	:param ratingGoodReviewVoteCount: Количество отзывов
	:param ratingKinopoisk: Рейтинг фильма
	:param ratingKinopoiskVoteCount: Количество отзывов
	:param ratingImdb: Рейтинг фильма в IMDB
	:param ratingImdbVoteCount: Количество отзывов
	:param ratingFilmCritics: Рейтинг фильма в критике
	:param ratingFilmCriticsVoteCount: Количество отзывов
	:param ratingAwait: Рейтинг фильма
	:param ratingAwaitCount: Количество отзывов
	:param ratingRfCritics: Рейтинг фильма в критике
	:param ratingRfCriticsVoteCount: Количество отзывов
	:param webUrl: Ссылка на страницу фильма
	:param year: Год выпуска
	:param filmLength: Длительность фильма
	:param slogan: Слоган
	:param description: Описание фильма
	:param shortDescription: Краткое описание фильма
	:param editorAnnotation: Аннотация режиссера
	:param isTicketsAvailable: Есть ли билеты
	:param productionStatus: Статус производства
	:param type: Тип медиа
	:param ratingMpaa: Рейтинг MPAA
	:param ratingAgeLimits: Возрастные ограничения
	:param countries: Страны
	:param genres: Жанры
	:param hasImax: Есть ли IMAX
	:param has3D: Есть ли 3D
	:param lastSync: Дата последнего обновления
	:param startYear: Год начала выпуска
	:param endYear: Год окончания выпуска
	:param serial: Сериал?
	:param shortFilm: Короткометражка?
	:param completed: Завершен?

	"""
	kinopoiskId: NonNull[int]
	kinopoiskHDId: Optional[str]
	imdbId: Optional[str]
	nameRu: Optional[str]
	nameEn: Optional[str]
	nameOriginal: Optional[str]
	posterUrl: NonNull[str]
	posterUrlPreview: NonNull[str]
	coverUrl: Optional[str]
	logoUrl: Optional[str]
	reviewsCount: int = 0
	ratingGoodReview: Optional[int]
	ratingGoodReviewVoteCount: Optional[int]
	ratingKinopoisk: Optional[float]
	ratingKinopoiskVoteCount: Optional[int]
	ratingImdb: Optional[float]
	ratingImdbVoteCount: Optional[int]
	ratingFilmCritics: Optional[float]
	ratingFilmCriticsVoteCount: Optional[int]
	ratingAwait: Optional[float]
	ratingAwaitCount: Optional[int]
	ratingRfCritics: Optional[float]
	ratingRfCriticsVoteCount: Optional[int]
	webUrl: NonNull[str]
	year: Optional[int]
	filmLength: Optional[int]
	slogan: Optional[str]
	description: Optional[str]
	shortDescription: Optional[str]
	editorAnnotation: Optional[str]
	isTicketsAvailable: bool = False
	productionStatus: Optional[ProductionStatus]
	type: Optional[MovieType]
	ratingMpaa: Optional[str]
	ratingAgeLimits: Optional[str]
	hasImax: Optional[bool]
	has3D: Optional[bool]
	lastSync: datetime
	countries: list[Country] = []
	genres: list[Genre] = []
	startYear: Optional[int]
	endYear: Optional[int]
	serial: Optional[bool]
	shortFilm: Optional[bool]
	completed: Optional[bool]

	def add_country(self, country: Union[Country, list[Country]]):
		if isinstance(country, list):
			self.countries.extend(country)
		else:
			self.countries.append(country)

	def add_genres(self, genres: Union[Genre, list[Genre]]):
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
