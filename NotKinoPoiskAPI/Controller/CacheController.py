import datetime
import hashlib
import os
import pickle
import platform
from pathlib import Path
from typing import Optional, Union

from decouple import config


class CacheController:
	cache_path: Path
	cache_lifetime: int

	def __init__(self, cache_path: Optional[Union[Path, str]] = None, lifetime: int = 7):
		if cache_path is None:
			ROOT = Path(__file__).parent.parent
			cache_path = config('NKPA_CACHE_DIR', cast=str, default=ROOT / 'Data/Cache')
		self._set_cache_path(cache_path)
		self.cache_lifetime = config('NKPA_CACHE_LIFE', cast=int, default=lifetime)

	def _set_cache_path(self, path):
		self.cache_path = Path(path)
		self.cache_path.mkdir(parents=True, exist_ok=True)

	def get_cache_file(self, data):
		data_hash = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
		return self.cache_path / f'{data_hash.__str__()}.pickle'

	def set_cache(self, name, data):
		cache_file = self.get_cache_file(name)
		with open(cache_file, 'wb') as f:
			pickle.dump(data, f)

	def get_cache(self, name):
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
		Try to get the date that a file was created, falling back to when it was
		last modified if that isn't possible.
		See http://stackoverflow.com/a/39501288/1709587 for explanation.
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
