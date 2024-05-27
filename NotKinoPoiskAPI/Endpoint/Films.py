from typing import Optional, Union

from requests import Session

from NotKinoPoiskAPI.Endpoint.NKPA import NKPA
from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Controller.ProxyController import ProxyController
from NotKinoPoiskAPI.Enums.CollectionType import CollectionType
from NotKinoPoiskAPI.Enums.FilmsFilterOrder import FilmFilterOrder
from NotKinoPoiskAPI.Enums.ImageType import ImageType
from NotKinoPoiskAPI.Enums.MovieType import MovieType
from NotKinoPoiskAPI.Enums.KpMonth import KpMonth
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
		"""
		Конструктор класса

		:param str api_key: API-Key для подключения.
		:param ProxyController proxy: Прокси для подключения.
		:param Session session: Сессия для запросов.
		:param str user_agent: User-Agent для запросов.
		:param dict headers: Дополнительные заголовки.
		:param int timeout: Время ожидания ответа.
		:param str cache_path: Путь к папке кеша.
		"""
		super().__init__(api_key=api_key, proxy=proxy, user_agent=user_agent, headers=headers, session=session,
		                 cache_path=cache_path, timeout=timeout)

	def get_film(self, film_id: int) -> Film:
		"""
		Метод для получения информации о фильме
		Данный эндпоинт возвращает базовые данные о фильме. Поле lastSync показывает дату последнего обновления данных.

		:Endpoint: /api/v2.2/films/{id}
		:param int film_id: ID фильма.
		:return: Информация о фильме
		:rtype: Film
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}')), Film)

	def get_seasons(self, film_id: int) -> SeasonResponse:
		"""
		Метод для получения информации о сезонах фильма

		:Endpoint: /api/v2.2/films/{id}/seasons
		:param int film_id: ID фильма.
		:return: Информация о сезонах фильма
		:rtype: SeasonResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/seasons')),
		                                       SeasonResponse)

	def get_film_facts(self, film_id: int) -> FactResponse:
		"""
		Данный эндпоинт возвращает список фактов и ошибок в фильме.

		:Endpoint: /api/v2.2/films/{id}/facts
		:param int film_id: ID фильма.
		:return:  Возвращает список фактов и ошибок в фильме
		:rtype: FactResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/facts')), FactResponse)

	def get_distributions(self, film_id: int) -> DistributionResponse:
		"""
		Данный эндпоинт возвращает данные о прокате в разных странах.

		:Endpoint: /api/v2.2/films/{id}/distributions
		:param int film_id: ID фильма.
		:return: Возвращает данные о прокате в разных странах
		:rtype: DistributionResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/distributions')),
		                                       DistributionResponse)

	def get_box_office(self, film_id: int) -> BoxOfficeResponse:
		"""
		Данный эндпоинт возвращает данные о кассовых сборах фильма.

		:Endpoint: /api/v2.2/films/{id}/box_office
		:param int film_id: ID фильма.
		:return: Возвращает данные о кассовых сборах фильма
		:rtype: BoxOfficeResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/box_office')),
		                                       BoxOfficeResponse)

	def get_film_awards(self, film_id: int) -> AwardResponse:
		"""
		Данный эндпоинт возвращает данные о наградах и премиях фильма.

		:Endpoint: /api/v2.2/films/{id}/awards
		:param int film_id: ID фильма.
		:return: Возвращает данные о наградах и премиях фильма
		:rtype: AwardResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/awards')),
		                                       AwardResponse)

	def get_film_videos(self, film_id: int) -> VideoResponse:
		"""
		Данный эндпоинт возвращает трейлеры, тизеры, видео для фильма по kinopoisk film id. В данный момент доступно три site:

		- YOUTUBE - в этом случае url это просто ссылка на youtube видео.
		- YANDEX_DISK - в этом случае url это ссылка на yandex disk.
		- KINOPOISK_WIDGET - в этом случае url это ссылка на кинопоиск виджет. Например https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1.

		Если вы хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:

.. code-block:: html
	:caption: Подключение виджета на сайт
	:linenos:

	<script src="https://unpkg.com/@ungap/custom-elements-builtin"></script>
	<script type="module" src="https://unpkg.com/x-frame-bypass"></script>
	<iframe is="x-frame-bypass" src="https://widgets.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&autoplay=1&cover=1" width="500" height="500"></iframe>

:Endpoint: /api/v2.2/films/{id}/videos
:param int film_id: ID фильма.
:return: возвращает трейлеры, тизеры, видео для фильма
:rtype: VideoResponse
"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/videos')),
		                                       VideoResponse)

	def get_similars(self, film_id: int) -> RelatedFilmResponse:
		"""
		Данный эндпоинт возвращает похожие фильмы.

		:Endpoint: /api/v2.2/films/{id}/similars
		:param int film_id: ID фильма.
		:return: Возвращает похожие фильмы
		:rtype: RelatedFilmResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/similars')),
		                                       RelatedFilmResponse)

	def get_images(self, film_id: int, image_type: ImageType = ImageType.STILL, page: int = 1) -> ImageResponse:
		"""
		Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит не более чем 20 фильмов.

		Доступные изображения:

		* STILL - кадры
		* SHOOTING - изображения со съемок
		* POSTER - постеры
		* FAN_ART - фан-арты
		* PROMO - промо
		* CONCEPT - концепт-арты
		* WALLPAPER - обои
		* COVER - обложки
		* SCREENSHOT - скриншоты

		:Endpoint: /api/v2.2/films/{id}/images
		:param int film_id: ID фильма.
		:param ImageType image_type: Тип изображения.
		:param int page: Номер страницы.
		:return: Возвращает изображения связанные с фильмом с пагинацией
		:rtype: ImageResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/images', type=image_type.name, page=page)),
			ImageResponse)

	def get_reviews(self, film_id: int, page: int = 1, order: ReviewOrder = ReviewOrder.DATE_DESC) -> ReviewResponse:
		"""
		Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.

		:Endpoint: /api/v2.2/films/{id}/reviews
		:param int film_id: ID фильма.
		:param int page: Номер страницы.
		:param ReviewOrder order: Сортировка.
		:return: Возвращает список рецензии зрителей с пагинацией
		:rtype: ReviewResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/reviews', page=page, order=order.name)),
			ReviewResponse)

	def get_external_sources(self, film_id: int, page: int = 1) -> ExternalSourceResponse:
		"""
		Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

		:Endpoint: /api/v2.2/films/{id}/external_sources
		:param int film_id: ID фильма.
		:param int page: Номер страницы.
		:return: Возвращает список сайтов с пагинацией
		:rtype: ExternalSourceResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/external_sources', page=page)), ExternalSourceResponse)

	def get_collections(self, col_type: CollectionType = CollectionType.TOP_POPULAR_ALL,
	                    page: int = 1) -> FilmCollectionResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

		:Endpoint: /api/v2.2/films/collections
		:param CollectionType col_type: Тип коллекции
		:param int page: Номер страницы
		:return: Возвращает список фильмов с пагинацией
		:rtype: FilmCollectionResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/collections', type=col_type.name, page=page)),
			FilmCollectionResponse)

	def get_premieres(self, year: int, month: Union[KpMonth, int]) -> PremiereResponse:
		"""
		Данный эндпоинт возвращает список кинопремьер. Например https://www.kinopoisk.ru/premiere/

		:Endpoint: /api/v2.2/films/premieres
		:param int year: Год
		:param KpMonth month: Месяц. Либо в виде объекта PremiereMonth. Либо цифра от 1 до 12
		:return: Возвращает список кинопремьер
		:rtype: PremiereResponse
		"""
		if isinstance(month, KpMonth):
			month = month.name
		elif isinstance(month, int):
			if month < 1 or month > 12:
				raise ValueError('month must be in range 1 to 12')
			month = KpMonth(month).name
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/premieres', year=year, month=month)), PremiereResponse)

	def get_filters(self) -> FiltersResponse:
		"""
		Возвращает список id стран и жанров, которые могут быть использованы в /api/v2.2/films

		:Endpoint: /api/v2.2/films/filters
		:return: Возвращает список id стран и жанров
		:rtype: FiltersResponse
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url('films/filters')), FiltersResponse)

	def get_films(self, countries: Optional[Union[int, list[int], str]] = None,
	              genres: Optional[Union[int, list[int], str]] = None, imdbId: Optional[str] = None,
	              keyword: Optional[str] = None, order: FilmFilterOrder = FilmFilterOrder.RATING,
	              type: MovieType = MovieType.ALL, ratingFrom: float = 0, ratingTo: float = 10, yearFrom: int = 1000,
	              yearTo: int = 3000, page: int = 1) -> FilmSearchByFiltersResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный эндпоинт не возращает более 400 фильмов. Используй /api/v2.2/films/filters чтобы получить id стран и жанров.

		.. note::

			На данный момент можно указать не более одной страны и жанра.

		:Endpoint: /api/v2.2/films
		:param Optional[Union[int, list[int], str]] countries: список id стран разделенные запятой. Например countries=1,2,3. На данный момент можно указать не более одной страны.
		:param Optional[Union[int, list[int], str]] genres: список id жанров разделенные запятой. Например genres=1,2,3. На данный момент можно указать не более одного жанра.
		:param Optional[str] imdbId: ID с IMDB
		:param Optional[str] keyword: ключевое слово, которое встречается в названии фильма
		:param FilmFilterOrder order: сортировка (RATING, NUM_VOTE, YEAR), по умолчанию: RATING
		:param MovieType type: тип фильма (FILM, TV_SHOW, TV_SERIES, MINI_SERIES, ALL), по умолчанию: ALL
		:param float ratingFrom: минимальный рейтинг, по умолчанию: 0
		:param float ratingTo: максимальный рейтинг, по умолчанию: 10
		:param int yearFrom: минимальный год, по умолчанию: 1000
		:param int yearTo: максимальный год, по умолчанию: 3000
		:param int page: номер страницы, по умолчанию: 1
		:return: Возвращает список фильмов с пагинацией
		:rtype: FilmSearchByFiltersResponse
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

		:Endpoint: /api/v2.1/films/{id}/sequels_and_prequels
		:param int film_id:
		:return: Возвращает список частей, что связаны с фильмом
		:rtype: FilmSequelsAndPrequelsResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/sequels_and_prequels', '2.1')),
			FilmSequelsAndPrequelsResponse)

	def search_by_keyword(self, keyword: str, page: int = 1) -> FilmSearchResponse:
		"""
		Поиск фильмов и сериалов по ключевому слову. Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

		:Endpoint: /api/v2.1/films/search-by-keyword
		:param str keyword: ключивые слова для поиска
		:param int page: номер страницы
		:return: Возвращает список фильмов с пагинацией
		:rtype: FilmSearchResponse
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url('films/search-by-keyword', '2.1', keyword=keyword, page=page)),
			FilmSearchResponse)

	def get_releases(self, year: int, month: Union[KpMonth, int], page: int = 1) -> DigitalReleaseResponse:
		"""
		Данный эндпоинт возвращает список цифровых релизов. Например https://www.kinopoisk.ru/comingsoon/digital/

		:Endpoint: /api/v2.1/films/releases
		:param int year: Год
		:param Union[KpMonth, int] month: Месяц. Либо в виде объекта `KpMonth` (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER). Либо цифра от 1 до 12
		:return: Возвращает список цифровых релизов
		:rtype: DigitalReleaseResponse
		:raise ValueError: Если месяц вне диапазона от 1 до 12
		"""
		if isinstance(month, KpMonth):
			month = month.name
		elif isinstance(month, int):
			if month < 1 or month > 12:
				raise ValueError('месяц должен быть в диапазоне от 1 до 12')
			month = ObjectController.find_enum(str(month), KpMonth).name
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url('films/releases', '2.1', year=year, month=month, page=page)),
			DigitalReleaseResponse)
