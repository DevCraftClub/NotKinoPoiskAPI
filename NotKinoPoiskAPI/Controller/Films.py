from typing import Optional, Union

from requests import Session

from NotKinoPoiskAPI.Controller.NKPA import NKPA
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Enums.CollectionType import CollectionType
from NotKinoPoiskAPI.Enums.FilmsFilterOrder import FilmFilterOrder
from NotKinoPoiskAPI.Enums.ImageType import ImageType
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Enums.PremiereMonth import PremiereMonth
from NotKinoPoiskAPI.Enums.ReviewOrder import ReviewOrder
from NotKinoPoiskAPI.Responses.AwardResponse import AwardResponse
from NotKinoPoiskAPI.Responses.BoxOfficeResponse import BoxOfficeResponse
from NotKinoPoiskAPI.Responses.DigitalReleaseResponse import DigitalReleaseResponse
from NotKinoPoiskAPI.Responses.DistributionResponse import DistributionResponse
from NotKinoPoiskAPI.Responses.ExternalSourceResponse import ExternalSourceResponse
from NotKinoPoiskAPI.Responses.FactResponse import FactResponse
from NotKinoPoiskAPI.Responses.FilmCollectionResponse import FilmCollectionResponse
from NotKinoPoiskAPI.Responses.FilmSearchByFiltersResponse import FilmSearchByFiltersResponse
from NotKinoPoiskAPI.Responses.FilmSearchResponse import FilmSearchResponse
from NotKinoPoiskAPI.Responses.FilmSequelsAndPrequelsResponse import FilmSequelsAndPrequelsResponse
from NotKinoPoiskAPI.Responses.FiltersResponse import FiltersResponse
from NotKinoPoiskAPI.Responses.ImageResponse import ImageResponse
from NotKinoPoiskAPI.Responses.PremiereResponse import PremiereResponse
from NotKinoPoiskAPI.Responses.RelatedFilmResponse import RelatedFilmResponse
from NotKinoPoiskAPI.Responses.ReviewResponse import ReviewResponse
from NotKinoPoiskAPI.Responses.SeasonResponse import SeasonResponse
from NotKinoPoiskAPI.Responses.VideoResponse import VideoResponse
from NotKinoPoiskAPI.Types.Film import Film


class KpFilms(NKPA):
	"""
	Класс для работы непосредственно с Endpoint /films с API неофициального кинопоиска
	"""

	def __init__(self, api_key: Optional[str] = None, proxy: Optional[ProxyController] = None,
	             user_agent: Optional[str] = None,
	             headers: Optional[dict] = None,
	             session: Optional[Session] = None, cache_path: Optional[str] = None, timeout: int = 5):
		super().__init__(api_key=api_key, proxy=proxy, user_agent=user_agent, headers=headers, session=session,
		                 cache_path=cache_path, timeout=timeout)

	def get_film(self, film_id: int) -> Film:
		"""
		Метод для получения информации о фильме
		Данный эндпоинт возвращает базовые данные о фильме. Поле lastSync показывает дату последнего обновления данных.
		/api/v2.2/films/{id}
		:param film_id: ID фильма.
		:return: Film
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}')), Film)

	def get_seasons(self, film_id: int) -> SeasonResponse:
		"""
		Метод для получения информации о сезонах фильма
		/api/v2.2/films/{id}/seasons
		:param film_id: ID фильма.
		:return SeasonResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/seasons')),
		                                       SeasonResponse)

	def get_film_facts(self, film_id: int) -> FactResponse:
		"""
		Данный эндпоинт возвращает список фактов и ошибок в фильме.
		/api/v2.2/films/{id}/facts
		:param film_id: ID фильма.
		:return: FactResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/facts')), FactResponse)

	def get_distributions(self, film_id: int) -> DistributionResponse:
		"""
		Данный эндпоинт возвращает данные о прокате в разных странах.
		/api/v2.2/films/{id}/distributions
		:param film_id: ID фильма.
		:return: DistributionResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/distributions')),
		                                       DistributionResponse)

	def get_box_office(self, film_id: int) -> BoxOfficeResponse:
		"""
		Данный эндпоинт возвращает данные о кассовых сборах фильма.
		/api/v2.2/films/{id}/box_office
		:param film_id: ID фильма.
		:return BoxOfficeResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/box_office')),
		                                       BoxOfficeResponse)

	def get_film_awards(self, film_id: int) -> AwardResponse:
		"""
		Данный эндпоинт возвращает данные о наградах и премиях фильма.
		/api/v2.2/films/{id}/awards
		:param film_id: ID фильма.
		:return: AwardResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/awards')),
		                                       AwardResponse)

	def get_film_videos(self, film_id: int) -> VideoResponse:
		"""
		Данный эндпоинт возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id. В данный момент доступно три site:
		YOUTUBE - в этом случае url это просто ссылка на youtube видео.
		YANDEX_DISK - в этом случае url это ссылка на yandex disk.
		KINOPOISK_WIDGET - в этом случае url это ссылка на кинопоиск виджет. Например https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1. Если вы хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:

		<script src="https://unpkg.com/@ungap/custom-elements-builtin"></script>
		<script type="module" src="https://unpkg.com/x-frame-bypass"></script>
		<iframe is="x-frame-bypass" src="https://widgets.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&autoplay=1&cover=1" width="500" height="500"></iframe>
		/api/v2.2/films/{id}/videos
		:param film_id: ID фильма.
		:return: VideoResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/videos')),
		                                       VideoResponse)

	def get_similars(self, film_id: int) -> RelatedFilmResponse:
		"""
		Данный эндпоинт возвращает похожие фильмы.
		/api/v2.2/films/{id}/similars
		:param film_id: ID фильма.
		:return: RelatedFilmResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/similars')),
		                                       RelatedFilmResponse)

	def get_images(self, film_id: int, image_type: ImageType = ImageType.STILL, page: int = 1) -> ImageResponse:
		"""
		Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит не более чем 20 фильмов.
		Доступные изображения:
		- STILL - кадры
		- SHOOTING - изображения со съемок
		- POSTER - постеры
		- FAN_ART - фан-арты
		- PROMO - промо
		- CONCEPT - концепт-арты
		- WALLPAPER - обои
		- COVER - обложки
		- SCREENSHOT - скриншоты

		/api/v2.2/films/{id}/images
		:param film_id: ID фильма.
		:param image_type: Тип изображения.
		:param page: Номер страницы.
		:return: ImageResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/{film_id}/images', type=image_type.name, page=page)),
				ImageResponse)

	def get_reviews(self, film_id: int, page: int = 1, order: ReviewOrder = ReviewOrder.DATE_DESC) -> ReviewResponse:
		"""
		Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.
		/api/v2.2/films/{id}/reviews
		:param film_id: ID фильма.
		:param page: Номер страницы.
		:param order: Сортировка.
		:return: ReviewResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/{film_id}/reviews', page=page, order=order.name)),
				ReviewResponse)

	def get_external_sources(self, film_id: int, page: int = 1) -> ExternalSourceResponse:
		"""
		Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.
		/api/v2.2/films/{id}/external_sources
		:param film_id: ID фильма.
		:param page: Номер страницы.
		:return: ExternalSourceResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/{film_id}/external_sources', page=page)), ExternalSourceResponse)

	def get_collections(self, col_type: CollectionType = CollectionType.TOP_POPULAR_ALL,
	                    page: int = 1) -> FilmCollectionResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
		/api/v2.2/films/collections
		:param col_type: Тип коллекции
		:param page: Номер страницы
		:return FilmCollectionResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/collections', type=col_type.name, page=page)),
				FilmCollectionResponse)

	def get_premieres(self, year: int, month: Union[PremiereMonth, int]) -> PremiereResponse:
		"""
		Данный эндпоинт возвращает список кинопремьер. Например https://www.kinopoisk.ru/premiere/
		/api/v2.2/films/premieres
		:param year: Год
		:param month: Месяц. Либо в виде объекта PremiereMonth. Либо цифра от 1 до 12
		:return PremiereResponse
		"""
		if isinstance(month, PremiereMonth):
			month = month.name
		elif isinstance(month, int):
			if month < 1 or month > 12:
				raise ValueError('month must be in range 1 to 12')
			month = PremiereMonth(month).name
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/premieres', year=year, month=month)), PremiereResponse)

	def get_filters(self) -> FiltersResponse:
		"""
		Возвращает список id стран и жанров, которые могут быть использованы в /api/v2.2/films
		/api/v2.2/films/filters
		:return FiltersResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url('films/filters')), FiltersResponse)

	def get_films(self, countries: Optional[Union[int, list[int], str]] = None,
	              genres: Optional[Union[int, list[int], str]] = None, imdbId: Optional[str] = None,
	              keyword: Optional[str] = None, order: FilmFilterOrder = FilmFilterOrder.RATING,
	              type: MovieType = MovieType.ALL, ratingFrom: float = 0, ratingTo: float = 10, yearFrom: int = 1000,
	              yearTo: int = 3000, page: int = 1) -> FilmSearchByFiltersResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный эндпоинт не возращает более 400 фильмов. Используй /api/v2.2/films/filters чтобы получить id стран и жанров.
		/api/v2.2/films
		:param countries: список id стран разделенные запятой. Например countries=1,2,3. На данный момент можно указать не более одной страны.
		:param genres: список id жанров разделенные запятой. Например genres=1,2,3. На данный момент можно указать не более одного жанра.
		:param imdbId: ID с IMDB
		:param keyword: ключевое слово, которое встречается в названии фильма
		:param order: сортировка (RATING, NUM_VOTE, YEAR), по умолчанию: RATING
		:param type: тип фильма (FILM, TV_SHOW, TV_SERIES, MINI_SERIES, ALL), по умолчанию: ALL
		:param ratingFrom: минимальный рейтинг, по умолчанию: 0
		:param ratingTo: максимальный рейтинг, по умолчанию: 10
		:param yearFrom: минимальный год, по умолчанию: 1000
		:param yearTo: максимальный год, по умолчанию: 3000
		:param page: номер страницы, по умолчанию: 1
		:return FilmSearchByFiltersResponse
		"""
		countries = ','.join(countries) if isinstance(countries, list) else str(countries) if isinstance(countries,
		                                                                                                 int) else countries
		genres = ','.join(genres) if isinstance(genres, list) else str(genres) if isinstance(genres, int) else genres
		return ObjectController.json_to_object(self.get_data(
				self.get_api_url('films', countries=countries, genres=genres, imdbId=imdbId, keyword=keyword,
				                 order=order.name, type=type.name, ratingFrom=ratingFrom, ratingTo=ratingTo,
				                 yearFrom=yearFrom, yearTo=yearTo, page=page)), FilmSearchByFiltersResponse)

	def get_film_prequels_and_sequels(self, film_id: int) -> FilmSequelsAndPrequelsResponse:
		"""
		Возвращает список частей, что связаны с фильмом
		/api/v2.1/films/{id}/sequels_and_prequels
		:param film_id:
		:return FilmSequelsAndPrequelsResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url(f'films/{film_id}/sequels_and_prequels', '2.1')),
				FilmSequelsAndPrequelsResponse)

	def search_by_keyword(self, keyword: str, page: int = 1) -> FilmSearchResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
		/api/v2.1/films/search-by-keyword
		:param keyword: ключивые слова для поиска
		:param page:
		:return FilmSearchResponse
		"""
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url('films/search-by-keyword', '2.1', keyword=keyword, page=page)),
				FilmSearchResponse)

	def get_releases(self, year: int, month: Union[PremiereMonth, int], page: int = 1) -> DigitalReleaseResponse:
		"""
		Данный эндпоинт возвращает список цифровых релизов. Например https://www.kinopoisk.ru/comingsoon/digital/
		:param year: Год
		:param month: Месяц. Либо в виде объекта PremiereMonth (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER). Либо цифра от 1 до 12
		:return DigitalReleaseResponse
		"""
		if isinstance(month, PremiereMonth):
			month = month.name
		elif isinstance(month, int):
			if month < 1 or month > 12:
				raise ValueError('month must be in range 1 to 12')
			month = PremiereMonth(month).name
		return ObjectController.json_to_object(
				self.get_data(self.get_api_url('films/releases', '2.1', year=year, month=month, page=page)),
				DigitalReleaseResponse)
