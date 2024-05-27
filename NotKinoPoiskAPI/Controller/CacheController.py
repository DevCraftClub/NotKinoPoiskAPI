import datetime
import hashlib
import os
import pickle
import platform
from pathlib import Path
from typing import Any, Optional, Union

from decouple import config


class CacheController:
	"""
	Класс по управлению за кешем.

	:param Path cache_path: Путь до папки с кешем
	:param int cache_lifetime: Время жизни кеша
	"""
	cache_path: Path
	"""Путь до папки с кешем"""
	cache_lifetime: int
	"""Время жизни кеша"""

	def __init__(self, cache_path: Optional[Union[Path, str]] = None, lifetime: int = 7):
		"""
		Инициализация кеша

		:param Union[Path, str] cache_path: Путь до папки с кешем
		:param int lifetime: Время жизни кеша
		"""
		if cache_path is None:
			ROOT = Path(__file__).parent.parent
			cache_path = config('NKPA_CACHE_DIR', cast=str, default=ROOT / 'Data/Cache')
		self.set_cache_path(cache_path)
		self.cache_lifetime = config('NKPA_CACHE_LIFE', cast=int, default=lifetime)

	def set_cache_path(self, path: Union[Path, str]):
		"""
		Установка пути до папки с кешем
		Создаёт папки на пути

		:param Union[Path, str] path: Путь до папки с кешем
		"""
		self.cache_path = Path(path) if isinstance(path, str) else path
		self.cache_path.mkdir(parents=True, exist_ok=True)

	def get_cache_file(self, file_name: str):
		"""
		Получить путь до файла с кешем

		:param str file_name: Данные для хэширования
		:return: Путь до файла с кешем
		:rtype: str
		"""
		data_hash = hashlib.md5(file_name.encode(encoding='UTF-8')).hexdigest()
		return self.cache_path / f'{data_hash.__str__()}.pickle'

	def set_cache(self, name: str, data: Any):
		"""
		Запись в кеш

		:param str name: Имя кеша
		:param Any data: Данные для кеша
		"""
		cache_file = self.get_cache_file(name)
		with open(cache_file, 'wb') as f:
			pickle.dump(data, f)

	def get_cache(self, name:str):
		"""
		Получить данные из кеша
		Если кеш не существует или время жизни кеша истекло, то возвращает None

		:param str name: Имя кеша
		:return: Данные из кеша, либо None (если данные отсутствуют или устарели)
		:rtype: dict | None
		"""
		cache_file = self.get_cache_file(name)
		if Path(cache_file).exists():
			file_created = datetime.datetime.fromtimestamp(CacheController.creation_date(cache_file))
			cache_lifetime = file_created + datetime.timedelta(days=self.cache_lifetime)
			today = datetime.datetime.now()
			date_diff = today - cache_lifetime
			if date_diff.days > self.cache_lifetime:
				os.remove(cache_file)
				return None
			else:
				with open(cache_file, 'rb') as f:
					return pickle.load(f)
		else:
			return None

	@staticmethod
	def creation_date(path_to_file):
		"""
		Возвращает дату создания файла

		:ref: https://stackoverflow.com/a/39501288/1709587

		:param str path_to_file: Путь до файла

		:return: Дата создания файла

		:rtype: float
		"""
		if platform.system() == 'Windows':
			return os.path.getctime(path_to_file)
		else:
			stat = os.stat(path_to_file)
			try:
				return stat.st_birthtime
			except AttributeError:
				# We're probably on Linux. No easy way to get creation dates here,
				# so we'll settle for when its content was last modified.
				return stat.st_mtime
