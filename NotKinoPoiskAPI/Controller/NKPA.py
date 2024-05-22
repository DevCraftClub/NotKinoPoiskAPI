import random
from dataclasses import dataclass
from typing import Any, Optional, Union
from urllib.parse import urlencode

from decouple import config
from requests import Session

from NotKinoPoiskAPI.Controller.Connector import Connector
from NotKinoPoiskAPI.Enums.CollectionType import CollectionType
from NotKinoPoiskAPI.Enums.ImageType import ImageType
from NotKinoPoiskAPI.Enums.PremiereMonth import PremiereMonth
from NotKinoPoiskAPI.Enums.ReviewOrder import ReviewOrder
from NotKinoPoiskAPI.Responses.ApiKeyResponse import ApiKeyResponse
from NotKinoPoiskAPI.Responses.AwardResponse import AwardResponse
from NotKinoPoiskAPI.Responses.BoxOfficeResponse import BoxOfficeResponse
from NotKinoPoiskAPI.Responses.DistributionResponse import DistributionResponse
from NotKinoPoiskAPI.Responses.ExternalSourceResponse import ExternalSourceResponse
from NotKinoPoiskAPI.Responses.FactResponse import FactResponse
from NotKinoPoiskAPI.Responses.FilmCollectionResponse import FilmCollectionResponse
from NotKinoPoiskAPI.Responses.FilmSearchByFiltersResponse import FilmSearchByFiltersResponse
from NotKinoPoiskAPI.Responses.FiltersResponse import FiltersResponse
from NotKinoPoiskAPI.Responses.ImageResponse import ImageResponse
from NotKinoPoiskAPI.Responses.PremiereResponse import PremiereResponse
from NotKinoPoiskAPI.Responses.RelatedFilmResponse import RelatedFilmResponse
from NotKinoPoiskAPI.Responses.ReviewResponse import ReviewResponse
from NotKinoPoiskAPI.Responses.SeasonResponse import SeasonResponse
from NotKinoPoiskAPI.Responses.VideoResponse import VideoResponse
from NotKinoPoiskAPI.Types.Film import Film


@dataclass
class NKPA:
	"""
	Класс работы с самим  Kinopoisk API Unofficial
	"""
	api_key: str
	session: Optional[Connector]
	api_link: str = 'https://kinopoiskapiunofficial.tech/api'

	def __init__(self, api_key: Optional[str] = None, proxy: Optional[Any] = None, user_agent: Optional[str] = None, headers: Optional[dict] = None,
	             session: Optional[Session] = None, timeout: int = 5):
		if api_key is None:
			api_keys_config = config.get('NKPA_API_KEY', default=None, cast=str)
			if api_keys_config is None:
				raise ValueError("API ключ не указан")
			api_key = random.choice(api_keys_config.split('||'))
		self.api_key = api_key
		self.session = Connector(api_key, proxy, session, user_agent, headers, timeout)

	def get_api_url(self, method: str, version: str = '2.2', **query) -> str:
		"""
		Метод для получения ссылки на метод API.
		:param version: Версия API.
		:param method: Метод API.
		"""
		url_query = f'?{urlencode(query)}' if query is not None and len(query) > 0 else ''
		return f"{self.api_link}/v{version}/{method}{url_query}"

	def get_data(self, link: str):
		"""
		Метод для отправки запроса с проверкой по квоте
		:param link: Ссылка на метод API.
		"""
		if self.get_api_info():
			return self.session.send(link)

	def get_api_info(self):
		"""
		Метод для получения информации о ключе
		/api/v1/api_keys/{apiKey}
		"""
		url = self.get_api_url(f'api_keys/{self.api_key}', '1')
		data: ApiKeyResponse
		data = self.session.send(url)
		if data.dailyQuota.used > data.dailyQuota.value:
			raise ValueError(f"Превышен лимит запросов\nИспользованный ключ: {self.api_key}")
		else:
			return True

	def get_film(self, film_id: int) -> Film:
		"""
		Метод для получения информации о фильме
		Данный эндпоинт возвращает базовые данные о фильме. Поле lastSync показывает дату последнего обновления данных.
		/api/v2.2/films/{id}
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}'))

	def get_seasons(self, film_id: int) -> SeasonResponse:
		"""
		Метод для получения информации о сезонах фильма
		/api/v2.2/films/{id}/seasons
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/seasons'))

	def get_film_facts(self, film_id: int) -> FactResponse:
		"""
		Данный эндпоинт возвращает список фактов и ошибок в фильме.
		/api/v2.2/films/{id}/facts
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/facts'))

	def get_distributions(self, film_id: int) -> DistributionResponse:
		"""
		Данный эндпоинт возвращает данные о прокате в разных странах.
		/api/v2.2/films/{id}/distributions
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/distributions'))

	def get_box_office(self, film_id: int) -> BoxOfficeResponse:
		"""
		Данный эндпоинт возвращает данные о кассовых сборах фильма.
		/api/v2.2/films/{id}/box_office
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/box_office'))

	def get_film_awards(self, film_id: int) -> AwardResponse:
		"""
		Данный эндпоинт возвращает данные о наградах и премиях фильма.
		/api/v2.2/films/{id}/awards
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/awards'))

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
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/videos'))

	def get_similars(self, film_id: int) -> RelatedFilmResponse:
		"""
		Данный эндпоинт возвращает похожие фильмы.
		/api/v2.2/films/{id}/similars
		:param film_id: ID фильма.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/similars'))

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
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/images', type=image_type.name, page=page))

	def get_reviews(self, film_id: int, page: int = 1, order: ReviewOrder = ReviewOrder.DATE_DESC) -> ReviewResponse:
		"""
		Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.
		/api/v2.2/films/{id}/reviews
		:param film_id: ID фильма.
		:param page: Номер страницы.
		:param order: Сортировка.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/reviews', page=page, order=order.name))

	def get_external_sources(self, film_id: int, page: int = 1) -> ExternalSourceResponse:
		"""
		Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.
		/api/v2.2/films/{id}/external_sources
		:param film_id: ID фильма.
		:param page: Номер страницы.
		"""
		return self.get_data(self.get_api_url(f'films/{film_id}/external_sources', page=page))

	def get_collections(self, col_type: CollectionType = CollectionType.TOP_POPULAR_ALL, page: int = 1) -> FilmCollectionResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
		/api/v2.2/films/collections
		:param col_type: Тип коллекции
		:param page: Номер страницы
		"""
		return self.get_data(self.get_api_url(f'films/collections', type=col_type.name, page=page))

	def get_premieres(self, year: int, month: PremiereMonth) -> PremiereResponse:
		"""
		Данный эндпоинт возвращает список кинопремьер. Например https://www.kinopoisk.ru/premiere/
		/api/v2.2/films/premieres
		"""
		return self.get_data(self.get_api_url(f'films/premieres', year=year, month=month.name))

	def get_filters(self) -> FiltersResponse:
		"""
		Возвращает список id стран и жанров, которые могут быть использованы в /api/v2.2/films
		/api/v2.2/films/filters
		"""
		return self.get_data(self.get_api_url('films/filters'))

	def get_films(self, countries: Union[int, list[int], str] = None, genres: Union[int, list[int], str] = None, order: int = None, type: int = None,
	              ratingFrom: str = 'RATING', page: int = 1) -> FilmSearchByFiltersResponse:
		"""
		Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный эндпоинт не возращает более 400 фильмов. Используй /api/v2.2/films/filters чтобы получить id стран и жанров.
		/api/v2.2/films
		TODO
		"""
