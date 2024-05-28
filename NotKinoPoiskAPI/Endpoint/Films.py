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

		Args:
			api_key (str): API-Key для подключения.
			proxy (ProxyController): Прокси для подключения.
			session (Session): Сессия для запросов.
			user_agent (str): User-Agent для запросов.
			headers (Dict): Дополнительные заголовки.
			timeout (int): Время ожидания ответа.
			cache_path (str): Путь к папке кеша.
		"""
		super().__init__(api_key=api_key, proxy=proxy, user_agent=user_agent, headers=headers, session=session,
		                 cache_path=cache_path, timeout=timeout)

	def get_film(self, film_id: int) -> Film:
		"""
		Метод для получения информации о фильме
		Данный эндпоинт возвращает базовые данные о фильме. Поле lastSync показывает дату последнего обновления данных.

		**Endpoint**: /api/v2.2/films/{id}

		Args:
			film_id (int): ID фильма.

		Returns:
			Film: Информация о фильме
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}')), Film)

	def get_seasons(self, film_id: int) -> SeasonResponse:
		"""
		Метод для получения информации о сезонах фильма

		**Endpoint**: /api/v2.2/films/{id}/seasons

		Args:
			film_id (int): ID фильма.

		Returns:
			SeasonResponse: Информация о сезонах фильма
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/seasons')),
		                                       SeasonResponse)

	def get_film_facts(self, film_id: int) -> FactResponse:
		"""
		Данный эндпоинт возвращает список фактов и ошибок в фильме.

		**Endpoint**: /api/v2.2/films/{id}/facts

		Args:
			film_id (int): ID фильма.

		Returns:
			FactResponse:  Возвращает список фактов и ошибок в фильме
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/facts')), FactResponse)

	def get_distributions(self, film_id: int) -> DistributionResponse:
		"""
		Данный эндпоинт возвращает данные о прокате в разных странах.

		**Endpoint**: /api/v2.2/films/{id}/distributions

		Args:
			film_id (int): ID фильма.

		Returns:
			DistributionResponse: Возвращает данные о прокате в разных странах
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/distributions')),
		                                       DistributionResponse)

	def get_box_office(self, film_id: int) -> BoxOfficeResponse:
		"""
		Данный эндпоинт возвращает данные о кассовых сборах фильма.

		**Endpoint**: /api/v2.2/films/{id}/box_office

		Args:
			film_id (int): ID фильма.

		Returns:
			BoxOfficeResponse: Возвращает данные о кассовых сборах фильма
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/box_office')),
		                                       BoxOfficeResponse)

	def get_film_awards(self, film_id: int) -> AwardResponse:
		"""
		Данный эндпоинт возвращает данные о наградах и премиях фильма.

		**Endpoint**: /api/v2.2/films/{id}/awards

		Args:
			film_id (int): ID фильма.

		Returns:
			AwardResponse: Возвращает данные о наградах и премиях фильма
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/awards')),
		                                       AwardResponse)

	def get_film_videos(self, film_id: int) -> VideoResponse:
		"""
		Данный эндпоинт возвращает трейлеры, тизеры, видео для фильма по kinopoisk film id. В данный момент доступно три site:

		- **YOUTUBE** - в этом случае url это просто ссылка на youtube видео.
		- **YANDEX_DISK** - в этом случае url это ссылка на yandex disk.
		- **KINOPOISK_WIDGET** - в этом случае url это ссылка на кинопоиск виджет. Например https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1.

		Если вы хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:
			<pre><code>
			```
			<script src="https://unpkg.com/@ungap/custom-elements-builtin"></script>
			<script type="module" src="https://unpkg.com/x-frame-bypass"></script>
			<iframe is="x-frame-bypass" src="https://widgets.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&autoplay=1&cover=1" width="500" height="500"></iframe>
			```
			</code></pre>

		**Endpoint**: /api/v2.2/films/{id}/videos

		Args:
			film_id (int): ID фильма.

		Returns:
			VideoResponse: Возвращает трейлеры, тизеры, видео для фильма
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url(f'films/{film_id}/videos')),
		                                       VideoResponse)

	def get_similars(self, film_id: int) -> RelatedFilmResponse:
		"""
		Данный эндпоинт возвращает похожие фильмы.

		**Endpoint**: /api/v2.2/films/{id}/similars

		Args:
			film_id (int): ID фильма.

		Returns:
			RelatedFilmResponse: Возвращает похожие фильмы
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

		**Endpoint**: /api/v2.2/films/{id}/images

		Args:
			film_id (int): ID фильма.
			image_type (ImageType): Тип изображения.
			page (int): Номер страницы.

		Returns:
			ImageResponse: Возвращает изображения связанные с фильмом с пагинацией
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/images', type=image_type.name, page=page)),
			ImageResponse)

	def get_reviews(self, film_id: int, page: int = 1, order: ReviewOrder = ReviewOrder.DATE_DESC) -> ReviewResponse:
		"""
		Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.

		**Endpoint**: /api/v2.2/films/{id}/reviews

		Args:
			film_id (int): ID фильма.
			page (int): Номер страницы.
			order (ReviewOrder): Сортировка.

		Returns:
			ReviewResponse: Возвращает список рецензии зрителей с пагинацией
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/reviews', page=page, order=order.name)),
			ReviewResponse)

	def get_external_sources(self, film_id: int, page: int = 1) -> ExternalSourceResponse:
		"""
		Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

		**Endpoint**: /api/v2.2/films/{id}/external_sources

		Args:
			film_id (int): ID фильма.
			page (int): Номер страницы.

		Returns:
			ExternalSourceResponse: Возвращает список сайтов с пагинацией
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/external_sources', page=page)), ExternalSourceResponse)

	def get_collections(self, col_type: CollectionType = CollectionType.TOP_POPULAR_ALL,
	                    page: int = 1) -> FilmCollectionResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

		**Endpoint**: /api/v2.2/films/collections

		Args:
			col_type (CollectionType): Тип коллекции.
			page (int): Номер страницы.

		Returns:
			FilmCollectionResponse: Возвращает список фильмов с пагинацией
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/collections', type=col_type.name, page=page)),
			FilmCollectionResponse)

	def get_premieres(self, year: int, month: Union[KpMonth, int]) -> PremiereResponse:
		"""
		Данный эндпоинт возвращает список кинопремьер. Например https://www.kinopoisk.ru/premiere/

		**Endpoint**: /api/v2.2/films/premieres

		Args:
			year (int): Год
			month (Union[KpMonth, int]): Месяц. Либо в виде объекта PremiereMonth. Либо цифра от 1 до 12

		Returns:
			PremiereResponse: Возвращает список кинопремьер
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

		**Endpoin**t: /api/v2.2/films/filters

		Returns:
			FiltersResponse: Возвращает список id стран и жанров
		"""
		return ObjectController.json_to_object(self.get_data(self.get_api_url('films/filters')), FiltersResponse)

	def get_films(self, countries: Optional[Union[int, list[int], str]] = None,
	              genres: Optional[Union[int, list[int], str]] = None, imdbId: Optional[str] = None,
	              keyword: Optional[str] = None, order: FilmFilterOrder = FilmFilterOrder.RATING,
	              type: MovieType = MovieType.ALL, ratingFrom: float = 0, ratingTo: float = 10, yearFrom: int = 1000,
	              yearTo: int = 3000, page: int = 1) -> FilmSearchByFiltersResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный эндпоинт не возращает более 400 фильмов. Используй /api/v2.2/films/filters чтобы получить id стран и жанров.

		!!! note

			На данный момент можно указать не более одной страны и жанра.

		**Endpoint**: /api/v2.2/films

		Args:
			countries (Union[int, List[int], str]): Список id стран разделенные запятой. Например countries=1,2,3. На данный момент можно указать не более одной страны.
			genres (Union[int, List[int], str]): Список id жанров разделенные запятой. Например genres=1,2,3. На данный момент можно указать не более одного жанра.
			imdbId (str): ID с IMDB
			keyword (str): Ключевое слово, которое встречается в названии фильма
			order (FilmFilterOrder): Сортировка (RATING, NUM_VOTE, YEAR), по умолчанию: RATING
			type (MovieType): Тип фильма (FILM, TV_SHOW, TV_SERIES, MINI_SERIES, ALL), по умолчанию: ALL
			ratingFrom (float): Минимальный рейтинг, по умолчанию: 0
			ratingTo (float): Максимальный рейтинг, по умолчанию: 10
			yearFrom (int): Минимальный год, по умолчанию: 1000
			yearTo (int): Максимальный год, по умолчанию: 3000
			page (int): Номер страницы, по умолчанию: 1

		Returns:
			FilmSearchByFiltersResponse: Возвращает список фильмов с пагинацией
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

		**Endpoint**: /api/v2.1/films/{id}/sequels_and_prequels

		Args:
			film_id (int): ID фильма.

		Returns:
			FilmSequelsAndPrequelsResponse: Возвращает список частей, что связаны с фильмом
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url(f'films/{film_id}/sequels_and_prequels', '2.1')),
			FilmSequelsAndPrequelsResponse)

	def search_by_keyword(self, keyword: str, page: int = 1) -> FilmSearchResponse:
		"""
		Поиск фильмов и сериалов по ключевому слову. Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

		**Endpoint**: /api/v2.1/films/search-by-keyword

		Args:
			keyword (str): ключивые слова для поиска
			page (int): номер страницы

		Returns:
			FilmSearchResponse: Возвращает список фильмов с пагинацией
		"""
		return ObjectController.json_to_object(
			self.get_data(self.get_api_url('films/search-by-keyword', '2.1', keyword=keyword, page=page)),
			FilmSearchResponse)

	def get_releases(self, year: int, month: Union[KpMonth, int], page: int = 1) -> DigitalReleaseResponse:
		"""
		Данный эндпоинт возвращает список цифровых релизов. Например https://www.kinopoisk.ru/comingsoon/digital/

		**Endpoint**: /api/v2.1/films/releases

		Args:
			year (int): Год
			month (Union[KpMonth, int]): Месяц. Либо в виде объекта `KpMonth` (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER). Либо цифра от 1 до 12
			page (int): номер страницы

		Returns:
			DigitalReleaseResponse: Возвращает список цифровых релизов
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
